import socket
import time
import threading
from time import sleep
#from mysql_connector import *
from pprint import pprint
from pprint import pformat
from queue import Queue
import sys
from threading import Thread, Lock


openPorts = []
hostnameOpenPorts = {} #storing result for one hostname and list of open ports
ipHostnameOpenPorts = {} #storing result for one ip, its hostname and opened ports
finalResults = {} #storing all results
targetHosts = {'ec2-18-185-241-122.eu-central-1.compute.amazonaws.com': '35.158.160.236'}
queue = Queue()

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

print("The scanner is started. Please wait for results")

def portscan(port):
    for hostname, ip in targetHosts.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:

            con = s.connect((ip, port))
            with print_lock:

                openPorts.append(port)
                hostnameOpenPorts = {"hostname": hostname,
                                "openports": list(set(openPorts))}
                result = {ip: hostnameOpenPorts}
                finalResults.update(result)
            con.close()
        except:
            pass


def threader():
    while True:
        worker = queue.get()
        portscan(worker)
        queue.task_done()


startTime = time.time()
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 10000):
    queue.put(worker)

queue.join()

print('Time taken:', time.time() - startTime)

print("----------------------------------------------")
pprint(finalResults)
print(len(finalResults))
