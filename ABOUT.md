```markdown
# About IMIN Cyber Framework

## Mission

IMIN Cyber Framework was built with one goal: **to provide security professionals with a powerful, all-in-one reconnaissance and exploitation toolkit** that runs anywhere Python runs — from Kali Linux to a Termux terminal on a phone.

No bloated dependencies. No GUI nonsense. Just raw terminal power with a cyberpunk aesthetic.

## Philosophy

1. **Speed** — Every module is multi-threaded. No one has time to wait.
2. **Coverage** — From OSINT to exploitation, the framework covers the full kill chain.
3. **Accessibility** — Runs on a $30 Android phone just as well as a $3000 workstation.
4. **Professional Output** — HTML reports that you can hand straight to a client.

## Architecture

```
imin_framework.py
│
├── Color Engine        → 15-color NEON theme system
├── Banner Engine       → 3 switchable ASCII art banners
├── Report Engine       → Multi-threaded logger + HTML generator
│
├── NetworkScanner      → Nmap wrapper + Python fallback
├── WebScanner          → Headers, tech, paths, SSL
├── VulnScanner         → 10+ vulnerability vectors
├── UserFinder          → 50+ OSINT platform search
├── DirectoryBruteforcer → Multi-threaded path discovery
├── PortScanner         → Native Python port scanner
├── DNSScanner          → Full DNS record enumeration
├── SubdomainScanner    → DNS subdomain discovery
├── HashTools           → Generation + cracking + identification
└── PayloadGenerator    → SQLi/XSS/LFI payloads + reverse shells
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v3.0 PRO** | 2026 | Complete rewrite — OOP architecture, 3 banners, HTML reports, 10+ vuln vectors, reverse shell generator, 50+ OSINT sites |
| **v2.0** | 2025 | Added vulnerability scanner, user finder, multi-threading |
| **v1.0** | 2024 | Initial release — basic network and web scanning |

## Contact

- **Telegram**: [@script_ill](https://t.me/script_ill)
- **Author**: IMIN

For feature requests, bug reports, or authorized collaboration — reach out on Telegram.

---

*"Stay secure. Stay dangerous."*
```