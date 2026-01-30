# AI Security Engineering Roadmap

## Phase 1: The Engineering Foundation (Current)

The goal of this phase is to master the "plumbing" required to serve, secure, and automate AI models. We are moving away from generic scripts to production-grade APIs and containerized environments.

### **1. Advanced Python & FastAPI**
* **Goal:** Move beyond basic logic to high-performance asynchronous programming.
* **Focus:** * Mastery of **Async/Await** for non-blocking AI model calls.
    * Implementation of **Pydantic** for strict data validation (Crucial for AI Security).
    * Building secure API endpoints for the Ubuntu Home AI using **FastAPI**.

### **2. Environment & Model Orchestration**
* **Goal:** Portability and isolation for different AI experiments.
* **Focus:**
    * **Docker:** Containerizing the FastAPI backend to ensure consistent deployment between the Ubuntu server and Raspberry Pi.
    * **Ollama/Local Hosting:** Managing local LLM lifecycles on the Ubuntu server to avoid third-party API dependencies.
    * **Linux Hardening:** Implementing "Least Privilege" for the `.venv` and Docker containers.

### **3. The RAG Foundation (Data as Context)**
* **Goal:** Teaching AI to use my specific technical data (e.g., Submarine Electronics Manuals or Security Logs).
* **Focus:**
    * Introduction to **Vector Databases** (ChromaDB or Pinecone).
    * Building a basic **Retrieval Augmented Generation (RAG)** pipeline to query local markdown files.

### **Current Project Milestone**
* **Project:** Secure AI Gateway
* **Description:** A FastAPI proxy that sits in front of the Home AI, logging every request for Root Cause Analysis and filtering potential prompt injection attempts.