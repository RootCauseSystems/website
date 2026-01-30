# Security Header Auditor (Experimental)

Run a real-time security audit of any domain directly from your browser.

<link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css"/>
<script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>

<div class="terminal-box" style="background: #1e1e1e; padding: 20px; border-radius: 8px; border: 1px solid #00ff00;">
    <input type="text" id="url-input" placeholder="google.com" style="width: 80%; padding: 10px; background: #333; color: #fff; border: 1px solid #555;">
    <button py-click="run_audit" style="padding: 10px; background: #00ff00; color: #000; font-weight: bold; cursor: pointer;">RUN AUDIT</button>

<pre id="output" style="color: #00ff00; ,margin-top: 20px; font-family: 'Courier New', monospace;"></pre>
</div>

<py-script>
import js
from pyodide.http import pyfetch
import asyncio

async def run_audit(event):
    url_input = js.document.getElementById("url-input").value
    output_div = js.document.getElementById("output")

    if not url_input.startswith("http"):
        url = f"https://{url_input}"
    else:
        url = url_input

    output_div.innerHTML = f"Analyzing {url}...\n"
    
    try:
        # Note: Browser security (CORS) may limit audits of ecternal sites
        # unless those sites allow cross-origin requests.
        response = await pyfetch(url, method="GET")
        headers = response.headers

        results = []
        check_list = ["Strict-Transport-Security", "Content-Security-Policy", "server"]

        for header in check_list:
            val = headers.get(header, "MISSING ❌")
            results.append(f"{header}: {val}")

        output_div.innerHTML += "\n".join(results)
    except Exception as e:
        output_div.innerHTML += f"Error: {str(e)}\n(Note: some sites block browser-based auditing via CORS policies.)"
</py-script>