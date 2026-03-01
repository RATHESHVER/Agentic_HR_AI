# Agentic AI Resume Screening System with RAG

## **Project Overview**

An end-to-end **Agentic AI-based Resume Screening and Job Matching System** that autonomously parses resumes, extracts skills, matches candidates to job roles using NLP, makes explainable **APPLY / IMPROVE** decisions, and provides personalized resume improvement guidance using **Retrieval-Augmented Generation (RAG)** with **FAISS** and a locally hosted **LLaMA-3 (Ollama)** model.

This project demonstrates modular AI agent design, vector search integration, and grounded LLM reasoning in a real-world hiring automation scenario.

---

## **Core Features**

- **Resume Parsing Agent** (PDF/DOCX support)
- **Skill Extraction using NLP**
- **Job Matching using TF-IDF + Cosine Similarity**
- **Autonomous Decision Agent (APPLY / IMPROVE)**
- **Explainable AI (match ratio, missing skills, reasoning)**
- **RAG Pipeline using FAISS**
- **Context-aware LLaMA-3 integration via Ollama**
- **Flask Web Application**
- **Modular Multi-Agent Architecture**

---

## **System Architecture**

User Upload Resume
↓
Resume Parsing Agent
↓
Skill Extraction Agent
↓
Job Matching Agent (TF-IDF + Cosine Similarity)
↓
Decision Agent (APPLY / IMPROVE)
↓
Result Page
↓
FAISS retrieves relevant job data (RAG)
↓
LLaMA-3 generates grounded resume guidance


---

## **Technology Stack**

### **Backend**
- Python
- Flask

### **Machine Learning / NLP**
- TF-IDF Vectorization
- Cosine Similarity
- Sentence Transformers
- FAISS (Vector Similarity Search)

### **LLM Integration**
- Ollama
- LLaMA-3 (Local Model)

### **Frontend**
- HTML
- CSS
- JavaScript

---

## **Project Structure**

```bash
Agentic_HR_AI/
│
├── app.py
│
├── agents/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── job_matcher.py
│   ├── decision_agent.py
│   ├── rag_agent.py
│   └── llm_agent.py
│
├── data/
│   └── jobs.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css




