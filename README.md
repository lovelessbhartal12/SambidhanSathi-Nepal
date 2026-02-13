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

> Replace the image path below with your actual workflow image file.

```plaintext
                ┌────────────────────┐
                │   Constitution PDF │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │  Text Chunking     │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │ Embedding Model    │
                │ (multilingual-e5)  │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │ FAISS Vector Store │
                └──────────┬─────────┘
                           ↑
                ┌──────────┴─────────┐
                │  User Query        │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │  Retriever (MMR)   │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │  LLM (Answer Gen)  │
                └──────────┬─────────┘
                           ↓
                ┌────────────────────┐
                │  Final Response    │
                └────────────────────┘
