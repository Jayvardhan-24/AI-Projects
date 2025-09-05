# 🚀 AI Projects Portfolio

This repository showcases my Artificial Intelligence projects.  
Currently, it includes:

1. **Conversational AI Chatbot with RAG (Retrieval-Augmented Generation)**
2. **Resume ATS Analyser**

> 💡 More AI projects will be added soon to this repository.

---

# 🤖 Project 1: Conversational AI Chatbot with RAG

## 📌 Overview
A **Conversational AI Chatbot** enhanced with **Retrieval-Augmented Generation (RAG)**.  
The chatbot can answer user queries by combining **LLM capabilities** with an external **knowledge base**.  
This ensures more accurate, reliable, and context-aware responses.

## ⚙️ How It Works
1. **User Query** → The user asks a question.  
2. **Retriever** → Searches the knowledge base (documents, PDFs, or database).  
3. **Generator (LLM)** → OpenAI LLM refines and generates a final response using both the query and retrieved context.  
4. **Response** → The chatbot delivers a precise and context-rich answer.

## 🛠️ Tech Stack
- **Python 3.10**
- **LangChain** – Retrieval-Augmented Generation pipeline
- **FAISS / Pinecone** – Vector database for knowledge retrieval
- **Google Gemini API** – LLM for natural language understanding & generation
- **Streamlit / Flask** – Web app interface

## 🚀 Features
- Context-aware conversational responses  
- Ability to ingest and query documents  
- Hybrid: combines information retrieval + generative AI  
- Deployable as a chatbot UI or API  

---

# 📄 Project 2: Resume ATS Analyser

## 📌 Overview
A **Streamlit-based web app** that analyzes resumes against job descriptions using **Google Gemini API**.  
It helps candidates improve their resumes by simulating how an **ATS (Applicant Tracking System)** evaluates them.

## ⚙️ How It Works
1. **Upload Resume (PDF)** → Converts the first page into image/text using `pdf2image`.  
2. **Enter Job Description** → User pastes the job description.  
3. **AI Evaluation** → Gemini API analyzes the match between resume & JD.  
4. **Results** →  
   - ATS Score (%)  
   - Missing Keywords  
   - Strengths & Weaknesses  
   - Suggestions for improvement  

## 🛠️ Tech Stack
- **Python 3.10**
- **Streamlit** – Interactive UI
- **pdf2image** – PDF parsing
- **Google Gemini API** – Resume scoring & analysis
- **dotenv** – API key management

## 🚀 Features
- Resume vs JD comparison  
- ATS score calculation  
- Feedback on missing skills & improvements  
- User-friendly web app interface  

---

# 📂 Repository Structure
```
AI-Projects/
│── chatbot-rag/               # Conversational AI with RAG
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
│── resume-ats-analyser/       # Resume ATS Analyser
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
│── .env.example               # Example API keys file
│── README.md                  # Portfolio-level documentation (this file)
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ai-projects.git
cd ai-projects
```

### 2️⃣ Setup virtual environment
```bash
conda create -p venv python=3.10 -y
conda activate ./venv
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables
Create a `.env` file in project root with your Gemini API key:
```
GOOGLE_API_KEY=your_gemini_api_key
```

### 5️⃣ Run a project
For Resume ATS Analyser:
```bash
cd resume-ats-analyser
streamlit run app.py
```

For Conversational Chatbot with RAG:
```bash
cd chatbot-rag
python app.py
```

---

# 🔑 Environment Variables
| Variable         | Description |
|------------------|-------------|
| `GOOGLE_API_KEY` | Your Gemini API key from [Google AI Studio](https://aistudio.google.com/) |

---

# 🐳 Optional: Run with Docker
```bash
docker build -t ai-projects .
docker run -p 8501:8501 ai-projects
```

---

# ⚠️ Troubleshooting
- **Poppler missing (PDF error)** → Install Poppler (`brew install poppler` on macOS).  
- **Quota exceeded (429)** → Upgrade Gemini API plan or wait for reset.  
- **Model not found** → Use latest supported model (`gemini-1.5-pro`).  

---

# 📜 License
MIT License – free to use, modify, and distribute.

