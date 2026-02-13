# 🇳🇵 SambidhanSathi – Nepal Constitution AI Assistant

An AI-powered **RAG (Retrieval-Augmented Generation)** assistant that helps users query and understand the **Constitution of Nepal (२०७२)** in Nepali and English.

This system uses **semantic search + multilingual embeddings + vector database + LLM** to provide accurate, context-aware answers from the constitution document.

---

## 🚀 Project Overview

SambidhanSathi is designed to:

- 📖 Answer constitutional queries
- 🔎 Retrieve relevant articles and clauses
- 🌐 Support multilingual queries (Nepali + English)
- 🤖 Provide AI-generated context-based responses
- 🧠 Use semantic search instead of keyword matching

---

## 🖼️ System Architecture (Workflow Diagram)

![Workflow Diagram](asserts\worflow.png)

## 🛠️ Tech Stack Used

| 🔹 Component       | 🔧 Technology                   |
| ------------------ | ------------------------------- |
| 🖥 Backend         | Python                          |
| 🧠 Framework       | LangChain                       |
| 📊 Embedding Model | `intfloat/multilingual-e5-base` |
| 🗄 Vector Database | FAISS                           |
| 🤖 LLM             | HuggingFace / Ollama            |
| 📄 PDF Processing  | PyMuPDF                         |
| 🌐 Optional UI     | Streamlit / FastAPI             |

## ⚠️ Limitations

- **Local Only:** Runs on a local system; no cloud or multi-user support.
- **Answer Accuracy:** Responses depend on RAG context from the PDF and may not always be fully accurate.
- **PDF Dependency:** Only the Constitution PDF in `data/` is used; missing sections affect results.
- **Resource Usage:** LLM and vector search may require high CPU/RAM.
- **No Real-Time Updates:** PDF changes require re-running `pdf_extractor.py`.

# SambidhanSathi-Nepal Project Structure

SambidhanSathi-Nepal/

├── data/  
├── embeddings/  
├── llm_loader.py  
├── retriever.py  
├── pdf_extractor.py  
├── main.py  
├── requirements.txt  
└── README.md

## 🚀 Installation Guide

Follow these steps to set up the **SambidhanSathi‑Nepal** project on your local machine.

### 🧠 Prerequisites

Make sure you have the following installed:

- **Python 3.10+**
- **Git**
- An **OpenAI API key** (to use LLM for generating answers)

### 📥 1. Clone the Repository

```bash
git clone https://github.com/lovelessbhartal12/SambidhanSathi-Nepal.git
cd SambidhanSathi-Nepal
```

### 🐍 2. Install Ollama

Follow instructions for your OS:

### 🐍 Install Ollama on Windows

1. Go to the official Ollama download page: [https://ollama.com/download](https://ollama.com/download)
2. Download the **Windows installer (`.exe`)**.
3. Run the downloaded installer and follow the on-screen instructions.
4. Once installed, you can verify by opening **Command Prompt** or **PowerShell** and running:

```powershell
ollama --version


```

### 🤝 Contributing

- Open issues for bugs or feature requests
- Fork the repository and submit pull requests
- Suggest improvements for multilingual support or accuracy

### 📄 References

- [LangChain Documentation](https://www.langchain.com/docs/)
- [FAISS Vector Database](https://faiss.ai/)
- [Ollama LLM](https://ollama.com/)

---

---

## ✨ Developed By

**Loblesh Bhartal**

> Passionate about AI, open-source, and building tools that make knowledge accessible.  
> This project is part of my effort to bring the **Nepal Constitution** closer to everyone through AI-powered assistance.

📬 Connect with me:

- GitHub: [lovelesshbhartal12](https://github.com/lovelessbhartal12)
- Email: loblessbhartal@gmail.com
- LinkedIn: [Loblesh Bhartal](https://www.linkedin.com/in/lobleshbhartal)
  l
