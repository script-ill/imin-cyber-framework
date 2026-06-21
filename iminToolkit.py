import os
import requests
from colorama import Fore, Style, init
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

report = []

# =========================
# LOG SYSTEM
# =========================
def log(data, color=Fore.WHITE):
    print(color + data)
    report.append(data)

def save_report():
    filename = "scan_report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(filename, "w") as f:
        for line in report:
            f.write(line + "\n")
    print(Fore.GREEN + f"\n[✓] Report saved: {filename}")

# =========================
# BANNER
# =========================
def banner():
    os.system("clear")
    print(Fore.GREEN + """



       -#*+=.                                      .=+*#-
       -@@@%%=.+:                              :+:=%%@@@-
       -@@@@@+                                    +@@@@@-
        *@@@@@*.     .=*+=:.        .:=+*=.     .*@@@@@*
         %@@@@@@@@@@@@@@@@%=        =%@@@@@@@@@@@@@@@@%
          .#@@@@@@@@@@@@@=            =@@@@@@@@@@@@@%:
             -*@@@@@@%=-                -=%@@@@@@*-


                  ⚡ IMIN CYBER FRAMEWORK PRO ⚡
                     Advanced Scanning Engine       Created by: IMIN | Telegram: @script_ill  | VERSION = 1.0.0


""" + Style.RESET_ALL)

    print(Fore.YELLOW + """
[1] Network Scan (Nmap)
[2] Web Scanner (AI)
[3] Vulnerability Scanner (Advanced)
[4] User Finder
[5] Directory Bruteforcer
[6] Port Scanner (Python)
[7] Save Report
[8] Exit
""")

# =========================
# NETWORK SCAN
# =========================
def network_scan():
    target = input(Fore.YELLOW + "Enter IP: ")
    log(f"\n[Network Scan] Target: {target}", Fore.CYAN)

    log("[+] Running Nmap Fast Scan...", Fore.GREEN)
    os.system(f"nmap -F {target}")

# =========================
# WEB SCAN (ADVANCED)
# =========================
def web_scanner():
    url = input(Fore.YELLOW + "Enter URL: ")

    if not url.startswith("http"):
        url = "http://" + url

    log(f"\n[Web Scan] Target: {url}", Fore.CYAN)

    try:
        r = requests.get(url, timeout=5)
        log("[+] Site reachable", Fore.GREEN)
    except:
        log("[-] Site unreachable", Fore.RED)
        return

    headers = r.headers

    # SECURITY HEADERS
    log("\n[Security Headers]", Fore.YELLOW)
    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    for h in security_headers:
        if h in headers:
            log(f"[+] {h} present", Fore.GREEN)
        else:
            log(f"[-] {h} missing", Fore.RED)

    # SERVER INFO
    log(f"\n[Server] {headers.get('Server', 'Unknown')}", Fore.CYAN)

    # BASIC VULNERABILITY HINTS
    log("\n[Vulnerability Hints]", Fore.YELLOW)

    if "X-Frame-Options" not in headers:
        log("[-] Possible Clickjacking risk", Fore.RED)

    if "Content-Security-Policy" not in headers:
        log("[-] Missing CSP (XSS risk)", Fore.RED)

    # PATH SCANNING (THREADED)
    log("\n[Path Discovery - Fast Mode]", Fore.YELLOW)

    paths = ["admin", "login", "dashboard", "backup", "config", "api", "test", "dev"]

    def scan_path(path):
        test_url = url + "/" + path
        try:
            res = requests.get(test_url, timeout=3)
            if res.status_code == 200:
                log(f"[!] Found: {test_url}", Fore.CYAN)
        except:
            pass

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scan_path, paths)


# =========================
# ADVANCED VULNERABILITY SCANNER
# =========================

def get_params(url):
    if "?" in url:
        return url.split("?")[0], url.split("?")[1].split("&")
    return url, ["id=1", "q=test"]  # default test params


# -------------------------
# SQL INJECTION (IMPROVED)
# -------------------------
def check_sqli(url):
    log("[*] Checking SQL Injection...", Fore.YELLOW)

    base, params = get_params(url)

    payloads = ["' OR '1'='1", "' OR 1=1--", "'--"]

    for param in params:
        key = param.split("=")[0]

        for p in payloads:
            test_url = f"{base}?{key}={p}"

            try:
                r = requests.get(test_url, timeout=5)

                errors = ["sql", "syntax", "mysql", "warning", "pdo"]

                if any(e in r.text.lower() for e in errors):
                    log(f"💀 SQLi detected: {test_url}", Fore.RED)
                    return

            except:
                pass

    log("[✓] No SQL Injection found", Fore.GREEN)


# -------------------------
# XSS (REFLECTION CHECK)
# -------------------------
def check_xss(url):
    log("[*] Checking XSS...", Fore.YELLOW)

    base, params = get_params(url)

    payload = "<script>alert(1)</script>"

    for param in params:
        key = param.split("=")[0]
        test_url = f"{base}?{key}={payload}"

        try:
            r = requests.get(test_url, timeout=5)

            if payload in r.text:
                log(f"💀 Reflected XSS: {test_url}", Fore.RED)
                return

        except:
            pass

    log("[✓] No XSS found", Fore.GREEN)


# -------------------------
# LFI (BASIC)
# -------------------------
def check_lfi(url):
    log("[*] Checking LFI...", Fore.YELLOW)

    base, params = get_params(url)

    payload = "../../../../etc/passwd"

    for param in params:
        key = param.split("=")[0]
        test_url = f"{base}?{key}={payload}"

        try:
            r = requests.get(test_url, timeout=5)

            if "root:" in r.text:
                log(f"💀 LFI detected: {test_url}", Fore.RED)
                return

        except:
            pass

    log("[✓] No LFI found", Fore.GREEN)


# -------------------------
# HEADER ANALYSIS
# -------------------------
def check_headers(url):
    log("[*] Checking Security Headers...", Fore.YELLOW)

    try:
        r = requests.get(url, timeout=5)
        headers = r.headers

        missing = []

        if "Content-Security-Policy" not in headers:
            missing.append("CSP")

        if "X-Frame-Options" not in headers:
            missing.append("X-Frame-Options")

        if "Strict-Transport-Security" not in headers:
            missing.append("HSTS")

        if missing:
            log(f"⚠️ Missing headers: {', '.join(missing)}", Fore.YELLOW)
        else:
            log("[✓] Headers look good", Fore.GREEN)

    except:
        log("[!] Header scan failed", Fore.RED)


# -------------------------
# MAIN SCANNER ENGINE
# -------------------------
def vulnerability_scanner():
    url = input(Fore.YELLOW + "Enter target URL: ")

    if not url.startswith("http"):
        url = "http://" + url

    log(f"\n[Advanced Vulnerability Scan] Target: {url}", Fore.CYAN)

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(check_sqli, url)
        executor.submit(check_xss, url)
        executor.submit(check_lfi, url)
        executor.submit(check_headers, url)

    log("[✓] Advanced scan completed", Fore.GREEN)

# =========================
# USER FINDER PRO (40+ SITES)
# =========================
def user_finder():
    username = input(Fore.YELLOW + "Enter username: ")
    log(f"\n[User Finder PRO] Searching for: {username}", Fore.CYAN)

    sites = {
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Medium": f"https://medium.com/@{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "VK": f"https://vk.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "About.me": f"https://about.me/{username}",
        "Disqus": f"https://disqus.com/by/{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "HackerNews": f"https://news.ycombinator.com/user?id={username}",
        "CodePen": f"https://codepen.io/{username}",
        "Replit": f"https://replit.com/@{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "500px": f"https://500px.com/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "BuyMeACoffee": f"https://www.buymeacoffee.com/{username}",
        "Linktree": f"https://linktr.ee/{username}",
        "CashApp": f"https://cash.app/${username}",
        "OK.ru": f"https://ok.ru/{username}",
        "Slack": f"https://{username}.slack.com",
        "WordPress": f"https://{username}.wordpress.com"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    def check(site, url):
        try:
            r = requests.get(url, headers=headers, timeout=5)

            # smarter detection
            if r.status_code == 200 and "not found" not in r.text.lower():
                log(f"💀 FOUND on {site}: {url}", Fore.GREEN)
            else:
                log(f"[✗] Not found on {site}", Fore.RED)

        except:
            log(f"[!] Error checking {site}", Fore.YELLOW)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for site, url in sites.items():
            executor.submit(check, site, url)

    log("[✓] User scan complete", Fore.GREEN)


# =========================
# DIRECTORY BRUTEFORCER
# =========================
def dir_bruteforce():
    url = input(Fore.YELLOW + "Enter target URL: ")

    if not url.startswith("http"):
        url = "http://" + url

    log(f"\n[Directory Bruteforce] Target: {url}", Fore.CYAN)

    # small but powerful wordlist (we can upgrade later)
    wordlist = [
        "admin", "login", "dashboard", "panel", "cpanel",
        "backup", "uploads", "images", "api", "config",
        "test", "dev", "old", "private", "secret"
    ]

    def check_dir(word):
        target = f"{url}/{word}"

        try:
            r = requests.get(target, timeout=5)

            if r.status_code in [200, 301, 302]:
                log(f"💀 FOUND: {target} [{r.status_code}]", Fore.GREEN)
            else:
                log(f"[{r.status_code}] {target}", Fore.WHITE)

        except:
            log(f"[!] Error: {target}", Fore.RED)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_dir, wordlist)

    log("[✓] Directory scan completed", Fore.GREEN)

# =========================
# PORT SCANNER (PYTHON)
# =========================
import socket

def port_scanner():
    target = input(Fore.YELLOW + "Enter IP or Domain: ")

    log(f"\n[Port Scanner] Target: {target}", Fore.CYAN)

    try:
        ip = socket.gethostbyname(target)
        log(f"[+] Resolved IP: {ip}", Fore.GREEN)
    except:
        log("[!] Could not resolve target", Fore.RED)
        return

    # Common important ports
    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-ALT"
    }

    def scan(port):
        try:
            sock = socket.socket()
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                service = ports.get(port, "Unknown")
                log(f"💀 OPEN: {port} ({service})", Fore.GREEN)

            sock.close()

        except:
            pass

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan, ports.keys())

    log("[✓] Port scan completed", Fore.GREEN)


# =========================
# MAIN LOOP
# =========================


while True:
    banner()
    choice = input(Fore.CYAN + "Select Option: ")

    if choice == "1":
        network_scan()

    elif choice == "2":
        web_scanner()

    elif choice == "3":
        vulnerability_scanner()

    elif choice == "4":
        user_finder()

    elif choice == "5":
        dir_bruteforce()

    elif choice == "6":
        port_scanner()

    elif choice == "7":
        save_report()

    elif choice == "8":
        print(Fore.RED + "Exiting...")
        break

    else:
        print(Fore.RED + "Invalid option!")

    input(Fore.YELLOW + "\nPress Enter to continue...")
