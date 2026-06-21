import requests
from colorama import Fore, Style, init

init(autoreset=True)

# ===== BANNER =====
print(Fore.CYAN + """
╔═══==============///////////////////////////═══════════════════════════════════=╗
║
### #   # ### #   #    #   # ##### ####   ####  ###   ###  #   # #   # ##### ####
 #  ## ##  #  ##  #    #   # #     #   # #     #     #   # ##  # ##  # #     #   #
 #  # # #  #  # # #    # # # ####  ####   ###  #     ##### # # # # # # ####  ####
 #  #   #  #  #  ##    ## ## #     #   #     # #     #   # #  ## #  ## #     #  #
### #   # ### #   #    #   # ##### ####  ####   ###  #   # #   # #   # ##### #   #

║               Cyber Tool v1.0
   Created by: Imin    |   Telegram: @script_kit
╚════============////////////////////////////══════════════════════════======═══╝
""" + Style.RESET_ALL)

url = input(Fore.YELLOW + "Enter target (https://example.com): ")

# Normalize URL
if not url.startswith("http"):
    url = "http://" + url

print(Fore.BLUE + "\n[+] Checking website...")

try:
    response = requests.get(url, timeout=5)
    print(Fore.GREEN + "[+] Website is reachable")
except:
    print(Fore.RED + "[-] Target not reachable")
    exit()

# HTTPS Check
if url.startswith("https"):
    print(Fore.GREEN + "[+] HTTPS detected")
else:
    print(Fore.RED + "[-] Not secure (HTTP)")

# Headers Check
print(Fore.CYAN + "\n=== Security Headers ===")

headers = response.headers
security_headers = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-XSS-Protection",
    "Strict-Transport-Security"
]

for h in security_headers:
    if h in headers:
        print(Fore.GREEN + f"[+] {h} present")
    else:
        print(Fore.RED + f"[-] {h} missing")

# Server Info
print(Fore.CYAN + "\n=== Server Info ===")
print(Fore.YELLOW + f"Server: {headers.get('Server', 'Unknown')}")

# Path Discovery
print(Fore.CYAN + "\n=== Path Discovery ===")

paths = ["admin", "login", "dashboard", "backup", "config", "api"]

for path in paths:
    test_url = url + "/" + path
    try:
        r = requests.get(test_url, timeout=5)
        if r.status_code == 200:
            print(Fore.YELLOW + f"[!] Found: {test_url}")
    except:
        pass

print(Fore.GREEN + "\n[✓] Scan Completed")
