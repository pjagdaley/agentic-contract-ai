from app.services.rag_instance import rag_service


class RetrievalAgent:

    def retrieve(self, question):

        if not rag_service.vector_store:
            return "No contract has been uploaded yet."

        docs = rag_service.vector_store.similarity_search(question, k=3)

        context = "\n\n".join([doc.page_content for doc in docs])

        return context