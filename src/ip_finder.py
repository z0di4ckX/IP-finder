import socket

def run():
    web = input("Entre the website: ")

    server = web

    if web[:7] == "http://":
        web = web[7:]
    
    if web[:8] == "https://":
        web = web[8:]

    lists = ["", "mail.", "ftp.", "drive.", "login.", "tftp.", 
    "ntp.", "udp.", "tcp.", "ttl.", "ssh.", "ssl.", "smtp.", "sip.",
    "pop.", "imap.", "prime.", "docs.", "slides.", "forms."]

    for x in lists:
        try:
            ip_resolver = socket.gethostbyname(x + web)
            
            print("[+] " + x + web + " " + ip_resolver + " found.")
        except:
            print("[-] Don't found " + x + web + " " + ip_resolver)

run()