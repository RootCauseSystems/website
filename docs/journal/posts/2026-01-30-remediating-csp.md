---
date: 2026-01-30
authors:
    - rob
categories:
    - Security
    - Python
---

# Remediation: Implementing Content Security Policy (CSP)

After establishing the initial perimeter, my internal audit tool flagged a missing **Content-Security-Policy (CSP)**. 

### **The Vulnerability**
Without a CSP, a site is susceptible to Cross-Site Scripting (XSS) and data injection. For a portfolio site utilizing PyScript, it is critical to define exactly where executable code can originate.

### **The Solution**
I implemented a **Strict CSP** using Cloudflare Transform Rules. This allows me to keep the site static on GitHub while injecting security headers at the "Edge" before the content reaches the user.

### **Verification**
I used my custom `auditor.py` script to verify the fix:
`Strict-Transport-Security: max-age=15552000`
`Content-Security-Policy: default-src 'self'; ...`

**Status:** Finding Remediated.