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


# =========================
# BANNER
# =========================
def banner():
    os.system("clear")
    print(Fore.CYAN + """
╔══════════════════════════════════════╗
║        ⚡ IMIN IP Scanner ⚡         ║
║   Created by: IMIN          
                Telegram: @script_kit              
      Fb: skript_kit                   ║
╚══════════════════════════════════════╝
""" + Style.RESET_ALL)

target = input("Enter target IP or website: ")

print("\n[1] Ping Test")
print("[2] Port Scan (Top 1000 ports)")

choice = input("Choose option: ")

if choice == "1":
    os.system(f"ping -c 4 {target}")

elif choice == "2":
    print("\nScanning ports...")
    os.system(f"nmap {target}")

else:
    print("Invalid choice")
