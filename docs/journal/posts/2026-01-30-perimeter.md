---
date: 2026-01-30
authors:
    - rob
categories:
    - Infrastructure
    - Security
---

# Establishing the Perimeter

The Log:

In my previous career, I spent two decades operating high-consequence nuclear systems where "Safety First" wasn't a slogan—it was the engineering baseline. As I pivot into AI Security, I am applying that same Systems-Level thinking to my own infrastructure.

The Objective: Build a public-facing portfolio and security toolset without creating a new attack surface.

The Logic of the Stack:

MkDocs (Static): By choosing a static site generator, I have eliminated the "Root Cause" of most web vulnerabilities: the database. No SQL means no SQL Injection.

Cloudflare (The Shield): Using a proxied DNS setup allows me to implement WAF rules that block automated scrapers and malicious bots before they ever touch my content.

PyScript (Client-Side Logic): To showcase tools like my Header Auditor, I am using WebAssembly (PyScript). This allows visitors to run my Python code in their browser sandbox, keeping my personal Ubuntu server completely isolated from the public web.

Current Status: Perimeter secure. First tool deployed. Now, we begin the deep dive into AI Adversarial testing.