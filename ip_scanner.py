import socket
import time
import threading

from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

#target = input('Enter the host to be scanned: ')
targetIp = ('ip') #enter the ips to be scanned
print('Starting scan on host: ', targetIp)


def portscan(port):
    for ip in targetIp:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((ip, port))
            with print_lock:
                print(port, 'is open on', ip )
            con.close()
        except:
            pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

for x in range(1000):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 65000):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)