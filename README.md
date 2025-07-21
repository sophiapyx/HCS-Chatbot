# RAG-Based-Chatbot-for-University-Health-Counselling-Services
This repository contains the source code for a retrieval-augmented generation (RAG) chatbot designed to support university students in navigating mental health and counselling services. Developed as part of the research paper "Bridging Gaps in AI-Assisted Help: Engaging Stakeholders in the Design and Development of a RAG-based Healthcare Chatbot"
Repository Structure

### 🔍 Overview

Students in post-secondary institutions face numerous barriers to accessing mental health services—ranging from long wait times and unclear navigation, to linguistic and cultural mismatches. This chatbot provides a more accessible, 24/7 solution that:

* Answers general questions about university counselling services
* Helps students locate relevant resources (e.g. self-help, appointments)
* Reduces misinformation by retrieving validated responses from a structured knowledge base

---

### 🛠️ Core Features

* **Retrieval-Augmented Generation (RAG):** Combines large language models (LLMs) with a context-aware information retrieval system
* **Custom Query Rewriting:** Refines vague user queries using conversation history
* **Context Ranking via Embeddings:** Uses semantic similarity to fetch the most relevant answer snippets
* **Transparent Fallbacks:** Gracefully handles uncertain queries with prompts for clarification
* **Modular Pipeline:** Components include query rewriting, context retrieval, embedding generation, and augmentation

---

### 📁 Repository Structure

* `question_answering_bot.py`: Main orchestrator of the chatbot logic
* `rewrite_user_query.py`: Rewrites ambiguous queries for better retrieval
* `retrieve_context.py`: Handles similarity-based retrieval from a structured QA dataset
* `generate_embeddings.py`: Generates OpenAI embeddings for questions
* `merge_data_with_embeddings.py`: Merges structured QA with pre-computed embeddings
* `set_key.py`: Handles API key setup for secure OpenAI access

---

### 📊 Data

This prototype uses a structured CSV dataset (`StructuredQA.csv`) developed in a sub-project for this chatbot to support retrieval component.  [Repo Url here]
