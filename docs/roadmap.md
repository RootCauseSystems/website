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

### 📌 Certification Overview
The CISSP is a globally recognized, advanced-level cybersecurity certification validating deep technical knowledge and managerial experience to effectively design, implement, and manage an organization's overall security posture. It proves competency in GRC (Governance, Risk, and Compliance) and business continuity.

### 🎯 Target Audience
* Mid-to-senior level cybersecurity professionals
* Security Managers, Security Architects, and Consultants
* Aspiring Chief Information Security Officers (CISOs)

### 🏗️ The 8 CISSP Domains
The curriculum is based on the [ISC2 CISSP Exam Outline](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) and covers eight core domains:

1. **Security and Risk Management (15%)**
2. **Asset Security (10%)**
3. **Security Architecture and Engineering (13%)**
4. **Communication and Network Security (13%)**
5. **Identity and Access Management (IAM) (13%)**
6. **Security Assessment and Testing (12%)**
7. **Security Operations (13%)**
8. **Software Development Security (10%)**

### 🛠️ Prerequisites & Requirements
To become fully certified, candidates must pass the exam and meet the following criteria:
* **Experience:** Minimum of 5 years of cumulative, paid work experience in at least two of the 8 CISSP domains. *(Note: A 4-year college degree or holding certain other certifications can waive one year of experience).*
* **Endorsement:** Requires endorsement by an active, certified ISC2 professional.
* *Don't have the experience yet?* You can pass the exam to become an **Associate of ISC2** and gain up to 6 years to acquire the required experience. 

### 📝 Exam Format
* **Format:** Computer Adaptive Testing (CAT) for English exams
* **Length:** 100 to 150 questions
* **Time Limit:** 3 hours
* **Passing Score:** 700 out of 1000 points

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