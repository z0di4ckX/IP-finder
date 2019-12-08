import socket

def run():
    web = input("Entre the website: ")

    scaner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = web

    if web[:7] == "http://":
        web = web[7:]
    
    if web[:8] == "https://":
        web = web[8:]

    lists = ["", "mail.", "ftp."]

    for x in lists:
        try:
            ip_resolver = socket.gethostbyname(x + web)
            
            print("[+] " + x + web + " " + ip_resolver + " found.")
        except:
            print("[-] Don't found " + x + web + " " + ip_resolver)

    #testing port
    def por_scan(port):
        try:
            scaner.connect((server, port))
            return True
        except:
            return False
    
    for x in range(25):
        if por_scan(x):
            print("Port", x, " is opne!")
        else:
            print("Port", x, " is closed")


run() 