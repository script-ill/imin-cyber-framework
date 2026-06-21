import requests
from colorama import Fore, Style

print(Fore.GREEN + "=== Imin L3 Vulnerability Scanner ===" + Style.RESET_ALL)

url = input("Enter target (with parameter, e.g. https://site.com/page?id=1): ")

# SQL Injection Test (SAFE DETECTION)
print("\n=== SQL Injection Test ===")

payload = "'"
test_url = url + payload

try:
    r = requests.get(test_url)
    
    errors = ["sql", "syntax", "mysql", "warning"]

    for err in errors:
        if err in r.text.lower():
            print(Fore.RED + f"[!] Possible SQL Injection indicator: {err}")
except:
    print("Request failed")


# XSS Test (Reflection Detection)
print("\n=== XSS Reflection Test ===")

xss_payload = "<script>alert(1)</script>"
test_url = url + xss_payload

try:
    r = requests.get(test_url)

    if xss_payload.lower() in r.text.lower():
        print(Fore.RED + "[!] Possible XSS reflection detected")
    else:
        print(Fore.GREEN + "[+] No reflection detected")
except:
    print("Request failed")


# Response Analysis
print("\n=== Response Clues ===")

keywords = ["error", "invalid", "admin", "flag"]

try:
    r = requests.get(url)

    for key in keywords:
        if key in r.text.lower():
            print(Fore.YELLOW + f"[!] Found keyword: {key}")
except:
    pass

print(Fore.GREEN + "\n[✓] Scan Complete")
