import tkinter as tk
import requests

def web_scan():
    url = entry.get()
    output.delete("1.0", tk.END)

    try:
        r = requests.get(url)
        output.insert(tk.END, "[+] Site reachable\n")
    except:
        output.insert(tk.END, "[-] Site unreachable\n")
        return

    headers = r.headers

    output.insert(tk.END, "\n[Headers]\n")
    for h in ["X-Frame-Options", "Content-Security-Policy"]:
        if h in headers:
            output.insert(tk.END, f"[+] {h} present\n")
        else:
            output.insert(tk.END, f"[-] {h} missing\n")

def vuln_scan():
    url = entry.get()
    output.delete("1.0", tk.END)

    try:
        r = requests.get(url + "'")
        if "error" in r.text.lower():
            output.insert(tk.END, "[!] Possible SQL Injection\n")
    except:
        pass

    payload = "<script>alert(1)</script>"
    try:
        r = requests.get(url + payload)
        if payload in r.text:
            output.insert(tk.END, "[!] Possible XSS\n")
    except:
        pass

# GUI window
root = tk.Tk()
root.title("ICF GUI Tool")

entry = tk.Entry(root, width=50)
entry.pack()

btn1 = tk.Button(root, text="Web Scan", command=web_scan)
btn1.pack()

btn2 = tk.Button(root, text="Vuln Scan", command=vuln_scan)
btn2.pack()

output = tk.Text(root, height=20, width=60)
output.pack()

root.mainloop()
