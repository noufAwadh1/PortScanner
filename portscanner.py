import socket
import sys
from datetime import datetime

remotServer = input('Enter a remote host scan: ')
#convert the domain to ip 
remotServerIP = socket.gethostbyname(remotServer)
print("-" * 60)
print("please waite ", remotServerIP)
print("-"*60)
t1 = datetime.now()
port =input("Enter ports number ").split()
try: 
    for port in (port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect_ex -> A non-blocking version of .connect() that returns an error code instead of throwing an exception.
        results = sock.connect_ex((remotServerIP, int(port)))
        if results ==0: # --> becouase connect_ex returns 0 if conencted or an error code 
            print("PORT: {}:    Openned".format(port))
            sock.close
        else:
            print("PORT: {} : Not Oppennd".format(port))
except KeyboardInterrupt:
    print(" keyboard interruption")
    sys.exit()
t2 = datetime.now()
total = t2 -t1 
print ("Scanning completed in ", total)
