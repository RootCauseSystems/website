# Integrated Academic & Engineering Roadmap

## Phase 1: WGU Degree Plan (Terms 3, 4, and 5)

### Term 3 (June 1, 2026 – November 30, 2026)
* **Ethics in Technology – D333:** Completed (Passed 06/25/2026)
* **Introduction to Cryptography – D830:** Target completion by August 29, 2026
* **Business of IT - Project Management – D324:** Scheduled August 29 – October 10, 2026
* **Managing Information Security – D832:** Scheduled October 10 – November 30, 2026

### Term 4 (December 1, 2026 – May 31, 2027)
* **Linux Foundations – D281**
* **Python for IT Automation – D522**
* **Introduction to AI and Security – D831**
* **Practical Applications of Prompt – D685**
* **Data Analytics - Applications – D492**

### Term 5 (June 1, 2027 – November 30, 2027)
* **Software Security and Testing – D385**
* **Managing Cloud Security – D320**
* **Penetration Testing and Vulnerability Analysis – D332**
* **Cybersecurity and Information Assurance Capstone – D833**

---
## Phase 2: CISSP (Certified Information Systems Security Professional)

The goal of this phase is to study for and pass the ISC2 CISSP Certification

**Goal:** **Study for and pass the ISC2 CISSP Certification**

## Phase 3: AI Security Engineering Roadmap (Post-Degree / Advanced Track)

The goal of this phase is to master the "plumbing" required to serve, secure, and automate AI models. We are moving away from generic scripts to production-grade APIs and containerized environments.

### **1. Advanced Python & FastAPI**
* **Goal:** Move beyond basic logic to high-performance asynchronous programming.
* **Focus:** 
    * Mastery of **Async/Await** for non-blocking AI model calls.
    * Implementation of **Pydantic** for strict data validation (Crucial for AI Security).
    * Building secure API endpoints for the Ubuntu Home AI using **FastAPI**.

### **2. Environment & Model Orchestration**
* **Goal:** Portability and isolation for different AI experiments.
* **Focus:**
    * **Docker:** Containerizing the FastAPI backend to ensure consistent deployment between the Ubuntu server and Raspberry Pi.
    * **Ollama/Local Hosting:** Managing local LLM lifecycles on the Ubuntu server to avoid third-party API dependencies.
    * **Linux Hardening:** Implementing "Least Privilege" for the `.venv` and Docker containers.

### **3. The RAG Foundation (Data as Context)**
* **Goal:** Teaching AI to use specific technical data (e.g., Submarine Electronics Manuals or Security Logs).
* **Focus:**
    * Introduction to **Vector Databases** (ChromaDB or Pinecone).
    * Building a basic **Retrieval Augmented Generation (RAG)** pipeline to query local markdown files.

### **Current Project Milestone**
* **Project:** Secure AI Gateway
* **Description:** A FastAPI proxy that sits in front of the Home AI, logging every request for Root Cause Analysis and filtering potential prompt injection attempts.