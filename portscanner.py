import sys
import socket
from datetime import datetime
import concurrent.futures



def isOpen(port):
    target = "";
    if len(sys.argv) == 3:
        if sys.argv[1] == "-h":
            target = socket.gethostbyname(sys.argv[2]);
        if sys.argv[1] == "-i":
            target = sys.argv[2];
    else:
        target = input("Host IP Address: ");
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    open = False
    if result ==0:
        open = True
    else:
        open = False
    s.close()
    return open;
    

if __name__ == '__main__':
    openports = [];
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for port, open in zip(range(1000), executor.map(isOpen, range(1000))):
            print("Port " + str(port) + " | " + str(open));
            if open == True: openports.append(port);
    if len(openports) > 0:
        print("Open Ports found:");
    for i in openports:
        print(str(i))
        
        