---
date: 2026-01-30 17:56:13
authors:
  - rob
categories:
  - Infrastructure
  - Troubleshooting
---

# The Deployment Circus: Debugging the "Invisible" Layers

Transitioning from hardware-centric nuclear systems to software-defined security has a steep learning curve—not in the logic, but in the "plumbing." This week's deployment felt like a three-ring circus, but it provided a masterclass in static site persistence.

### **The Clowns in the Ring**
* **The Oversized Asset:** A 5.5MB logo that initially choked the GitHub pipeline. 
* **The YAML Mirage:** Indentation errors in `.authors.yml` that caused the build to "go blind" to my professional identity.
* **The CSP Wall:** Implementing a "Default Deny" Content Security Policy that was so effective it blocked my own analytics and developer tools.

### **The Root Cause Analysis**
In the Navy, we never bypassed an interlock; we adjusted the setpoints until the system operated within safe parameters. I applied that same philosophy here—refining the CSP `connect-src` and tuning the `mkdocs-material` plugin until the automated build turned green.

**Status:** Perimeter secure. Identity verified. Resilience tested.