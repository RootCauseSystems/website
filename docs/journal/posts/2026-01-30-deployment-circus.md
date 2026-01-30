---
date: 2026-01-30
authors:
  - rob
categories:
  - Infrastructure
  - Troubleshooting
---

# The Deployment Circus: Lessons in Static Site Persistence

Getting a modern engineering portfolio live isn't just about writing code; it's about mastering the "invisible" infrastructure that connects the code to the user.

### **The Points of Failure**
1. **The 5MB Logo:** A nuclear-grade image size that choked the build pipeline. 
   * *The Fix:* A custom Python script using `Pillow` to compress the asset to <500KB.
2. **The YAML Maze:** Deprecated attributes (`align`) and sensitive indentation in `.authors.yml` led to multiple deployment failures.
3. **The CSP Wall:** A Content Security Policy so strict it blocked the site’s own identity and tools.

### **The Logic of the Pivot**
In submarine electronics, a "fault" is a puzzle to be solved with a schematic and a meter. In AI Security, the "schematic" is the build log, and the "meter" is the browser console. 

**Current Status:** Infrastructure stabilized. Identity verified. Perimeter secure.