# Conversational AI with RAG 🧠💬

## 📌 Objective
This project demonstrates how to build a Conversational AI system that answers questions based on custom data sources (text, PDF, JSON, or images).

It integrates open-source and proprietary LLMs with LangChain and Vector Databases to provide accurate, context-aware responses.

---

## ⚙️ Tech Stack
- **Frameworks**: LangChain, Gradio  
- **Vector DB**: Chroma, FAISS 
- **LLMs**: OpenAI (GPT-4/4o-mini)
- **Tools**: Prompt Engineering, Chains  

---

## 🚀 Features
- Ingests multiple document types  
- Embedding + VectorDB retrieval  
- Works with multiple LLMs  
- Simple Gradio chat interface  

---

## 🛠️ Setup & Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/conversational-ai-rag.git

cd conversational-ai-rag


2️⃣ Create virtual environment

python -m venv venv

source venv/bin/activate   # On Mac/Linux

venv\Scripts\activate      # On Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run Colab

colab notebook

## 🎯 Usage

Place your documents in the data/ folder.

Run the notebook Final_Gen-AI_Project_Jay.ipynb.

Choose your preferred LLM (OpenAI, HuggingFace, etc.).

Start chatting via the Gradio interface.

## 🔎 RAG Workflow

Document Loader → Load data (PDF, text, JSON, images)

Text Splitter → Chunk data for embedding

Embedding Model → Convert chunks into vector representations

VectorDB → Store & retrieve embeddings

LLM Integration → Answer questions using retrieval + prompt engineering

Gradio UI → Chat with your data
