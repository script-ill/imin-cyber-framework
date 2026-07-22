```markdown
## ⚡ Overview

**IMIN Cyber Framework** is a professional-grade, multi-layer penetration testing suite built in pure Python. It combines network scanning, web application security assessment, OSINT username enumeration, vulnerability detection, payload generation, and hash analysis — all in one powerful CLI framework with a cyberpunk neon interface.

### 🎯 Capabilities

| # | Module | Description |
|:-:|--------|-------------|
| 🌐 | **Network Scanner** | Nmap wrapper + Python fallback — port discovery, service detection, OS fingerprinting |
| 🌍 | **Web Scanner** | Security headers analysis, tech detection, path discovery, SSL/TLS audit |
| 💉 | **Vulnerability Scanner** | SQLi, XSS, LFI, RFI, CMDi, Open Redirect, CORS, HTTP methods, info disclosure |
| 🔍 | **User Finder (OSINT)** | Searches **50+ platforms** for username presence — social media, dev, gaming, crypto |
| 📂 | **Directory Bruteforcer** | Multi-threaded path discovery with smart wordlist generation |
| 🔌 | **Port Scanner** | Native Python multi-threaded port scanner with service identification |
| 📡 | **DNS Scanner** | Full DNS record enumeration — A, AAAA, MX, NS, TXT, SOA, CNAME |
| 🌐 | **Subdomain Scanner** | DNS-based subdomain discovery |
| 🔑 | **Hash Tools** | Hash generation, online cracking (MD5/SHA1), hash type identification |
| 💣 | **Payload Generator** | SQLi, XSS, LFI payloads + **9 reverse shell variants** |
| 📊 | **Save Report** | Generates professional **HTML report** with severity stats and findings |

### 🖥️ Interface

- **3 switchable cyberpunk neon banners**
- **Color-coded severity system** (CRITICAL → HIGH → MEDIUM → LOW → INFO)
- **Live progress tracking** with thread pools
- **Professional HTML report generation**

---

## ⚙️ Installation

### Requirements

- Python 3.7+
- Linux / Termux / macOS / Windows
- Internet connection (for API calls)

### Quick Install

```bash
# Clone or download the framework
git clone https://github.com/script-ill/imin-cyber-framework.git
cd imin-cyber-framework

# Install dependencies
pip install -r requirements.txt

# Run it
python imin_framework.py
```

### Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python git
pip install requests colorama
python imin_framework.py
```

---

## 🚀 Usage

```bash
python imin_framework.py
```

Navigate with the interactive menu:

```
    🌐 [01] Network Scan (Nmap)
    🌍 [02] Web Scanner
    💉 [03] Vulnerability Scanner
    🔍 [04] User Finder (OSINT)
    📂 [05] Directory Bruteforcer
    🔌 [06] Port Scanner (Python)
    📡 [07] DNS Scanner
    🌐 [08] Subdomain Scanner
    🔑 [09] Hash Tools
    💣 [10] Payload Generator
    📊 [11] Save Report
    🖼️ [12] Change Banner
    🚪 [13] Exit
```

**Example — User Finder:**

```
Enter option: 4
Enter username: johndoe

💀 FOUND on GitHub: https://github.com/johndoe
💀 FOUND on Twitter: https://twitter.com/johndoe
💀 FOUND on Instagram: https://instagram.com/johndoe
...
Found 24/50 profiles for: johndoe
```

**Example — Vulnerability Scan:**

```
Enter option: 3
Enter target URL: https://example.com

💀 SQL Injection! Parameter: id
💀 Reflected XSS! Parameter: search
💀 LFI! Parameter: file
⚠️ Missing headers: CSP, HSTS, X-Frame-Options
```

---

## 📊 Report Format

The framework generates professional **HTML reports** with:

- Severity distribution charts (CRITICAL / HIGH / MEDIUM / LOW / INFO)
- Timestamped findings with full details
- Complete session logs
- Cyberpunk-themed styling

---

## 📋 Requirements

```
requests>=2.28.0
colorama>=0.4.6
```

*Optional:*
- `nmap` — for full Network Scanner functionality (recommended)
- `dnspython` — for enhanced DNS resolution

---

## ⚠️ Legal Disclaimer

This tool is provided **strictly for authorized security testing and educational purposes only**. You must have explicit written permission before testing any system or network. Unauthorized access is illegal and punishable by law.

**The author (IMIN) assumes NO liability** for misuse or damages caused by this software.

---

## 🧠 Author

**IMIN** — Security Researcher & Penetration Tester

- Telegram: [@script_ill](https://t.me/script_ill)

---

## 📜 License

**IMIN Cyber Framework** is released under a **Proprietary License**.

You may **use** this software for authorized security testing and education.
You may **NOT** modify, distribute, sublicense, or sell this software without explicit written permission from the author.

See the [LICENSE](LICENSE) file for full terms.

```