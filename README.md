# keyhunter

![Hunt. Seek. Find](images/keyhunterdog.png)


A lightweight utility for **discovering and collecting keys/tokens** in HTML pages — intended for lab use and authorized security assessments.  

---

## 🔎 Overview

`keyhunter` scans HTML content (from live URLs or saved HTML files) to detect **sensitive patterns** such as API keys, tokens, secrets and other exposed credentials that appear in page markup, scripts or inline data. It helps detect accidental credential exposure on web pages and client-side code.

> ⚠️ **Legal notice:** Use this tool only against targets you own or have explicit permission to test (local projects, staging environments, or contracted engagements). Unauthorized use is illegal.

---

## ⚙️ Key Features (example)

- Fetches a web page (HTTP/HTTPS) and inspects its HTML for predefined patterns (API keys, tokens, strings like `secret`, `key`, `token`, etc.).  

> Note: adjust regexes/patterns to suit your environment and threat model.

---

## 📥 Installation

> Requires Python 3.6+.

```bash
# clone repository
git clone https://github.com/nailtpax/keyhunter.git
cd keyhunter

# install dependencies if requirements.txt exists
pip install -r requirements.txt
```
## 🙏 Credits

- Inspired by several open source security tools for secret detection.
- Thanks to my personal friend [@JoaoVitorBranco](https://github.com/JoaoVitorBranco) who contributed ideas to the code and has constantly encouraged me to improve my development skills.

Contributions, feedback, and improvements are always welcome.