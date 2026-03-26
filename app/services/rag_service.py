import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


class RAGService:

    def __init__(self):

        self.llm = ChatOpenAI(temperature=0)

        self.embedding_model = OpenAIEmbeddings()

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        self.vector_store = None

    def load_and_index(self, file_path):

        # Load PDF
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        # Split into chunks
        chunks = self.text_splitter.split_documents(documents)

        # Create vector DB
        self.vector_store = FAISS.from_documents(
            chunks,
            self.embedding_model
        )

        return len(chunks)

    def query(self, question):

        if not self.vector_store:
            return "No contract indexed yet."

        docs = self.vector_store.similarity_search(question, k=3)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
            You are a legal assistant.

            Answer the question based ONLY on the contract context below.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """

        response = self.llm.invoke(prompt)

        return response.content