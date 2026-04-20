# 🚀 Agentic AI for Contract Lifecycle Management

An end-to-end **Agentic AI system** that automates contract understanding, analysis, and risk detection using a multi-agent architecture powered by LLMs and Retrieval-Augmented Generation (RAG).

This project demonstrates **next-generation AI system design**, where multiple specialized agents collaborate to analyze legal documents and provide structured, actionable insights.

---

# 📌 Features

## 🔹 Core AI Capabilities

* 📄 Upload and index contract documents (PDF)
* 🤖 Ask questions about contracts (Q&A)
* ⚖️ Automated legal clause analysis
* 🚨 Risk detection and recommendations
* 📊 Structured JSON output for downstream systems

---

## 🔹 Agentic AI System

* 🧠 Multi-agent architecture:

  * Retrieval Agent (context extraction)
  * Analysis Agent (legal reasoning)
  * Risk Agent (risk detection)
* 🎯 Orchestrator for intelligent agent routing
* 🔄 Dynamic decision-making based on query intent

---

## 🔹 RAG (Retrieval-Augmented Generation)

* 📚 Contract indexing using embeddings
* 🔍 Semantic search using FAISS
* 🧩 Chunking using recursive text splitting
* 📌 Context-aware LLM responses

---

## 🔹 API Features

* ⚡ FastAPI-based REST APIs
* 📤 Contract upload endpoint
* 💬 Query endpoint with intelligent routing
* 🔐 Input validation using Pydantic
* 📄 Swagger UI for testing

---

## 🔹 Observability & Reliability

* 📜 Logging for queries and responses
* ⚠️ Error handling and safeguards
* 🔄 Graceful handling of missing data (no contract uploaded)

---

## 🔹 Deployment Features

* 🐳 Dockerized application
* ⚙️ Environment variable management (.env)
* 🔗 Production-ready API service

---

# 🛠️ Technology Stack

## 🔹 Backend & API

* FastAPI
* Uvicorn
* Pydantic

---

## 🔹 AI / LLM Layer

* LangChain
* OpenAI (ChatGPT / Embeddings)
* Prompt Engineering

---

## 🔹 Agentic AI Architecture

* Multi-Agent System Design

  * Retrieval Agent
  * Analysis Agent
  * Risk Agent
* Orchestrator Pattern (Agent Routing & Control Flow)

---

## 🔹 Retrieval-Augmented Generation (RAG)

* FAISS (Vector Database)
* OpenAI Embeddings
* Recursive Text Splitting (LangChain Text Splitters)

---

## 🔹 Data Processing

* PyPDF (Document Loading)
* Chunking & Semantic Indexing

---

## 🔹 DevOps & Deployment

* Docker
* Environment Management (.env, python-dotenv)

---

## 🔹 Observability & Reliability

* Python Logging
* Input Validation & Error Handling

---

## 🔹 Development Tools

* Python 3.10
* VS Code
* Git & GitHub

---

# 🏗️ Architecture

```text
User Query
     │
     ▼
FastAPI API Layer
     │
     ▼
Orchestrator (Decision Engine)
     │
     ├── Retrieval Agent → Fetch relevant contract context
     ├── Analysis Agent → Interpret legal meaning
     └── Risk Agent → Identify risks & recommendations
     │
     ▼
LLM (OpenAI)
     │
     ▼
Structured Response

```
# ☁️ Cloud Deployment

- AWS ECS (Fargate)  
- Application Load Balancer (ALB)  
- Amazon ECR  
- Docker  

---

# ⚙️ How to Run (Docker)

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd agentic-contract-ai
```

---

### 2️⃣ Create `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

---

### 3️⃣ Build Docker Image

```
docker build -t agentic-contract-ai .
```

---

### 4️⃣ Run Container

```
docker run -p 8000:8000 --env-file .env agentic-contract-ai
```

---

### 5️⃣ Access API

* Swagger UI: http://localhost:8000/docs

---

# 🧪 Usage

## 1️⃣ Upload Contract

* Use `/upload` endpoint
* Upload a PDF contract

---

## 2️⃣ Ask Questions

Use `/query` endpoint:

### Example Queries:

* What is the termination clause?
* What are the payment terms?
* What risks exist in this contract?

---

## 📥 Sample Input

```json
{
  "question": "What are the risks in this contract?"
}
```

---

## 📤 Sample Output

```json
{
  "risks": ["High penalty clause"],
  "missing_clauses": ["No dispute resolution clause"],
  "recommendations": ["Add arbitration clause"]
}
```

---

# 🧠 Key Highlights

* Built a **multi-agent AI system**, not just a chatbot
* Implemented **agent orchestration and decision routing**
* Designed **RAG-based knowledge layer for contracts**
* Delivered **structured, machine-readable outputs**
* Developed **production-ready, Dockerized API**

---

# 🔮 Future Enhancements

* LangGraph / CrewAI integration for advanced agent workflows
* Contract version comparison
* Clause classification using fine-tuned models
* UI dashboard (reuse from Project 1)
* Monitoring (Prometheus / Grafana)

---

# 👨‍💻 Author

Architected and built as a real-world AI platform illustrating enterprise architecture principles, cloud-native deployment, and scalable system design.
Deployed on AWS ECS (Fargate) with Application Load Balancer, following production-grade architecture patterns.


---
