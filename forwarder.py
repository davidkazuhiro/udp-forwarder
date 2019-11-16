from netifaces import interfaces, ifaddresses
from select import select
from socket import socket, AF_PACKET, SOCK_RAW, getprotobyname

interface = "eth0"
protocol = getprotobyname('udp')

print("\nPrinting Interfaces...")
for interface in interfaces():
    print(interface)
    for entry in ifaddresses(interface):
        print(ifaddresses(interface)[entry][0]['addr'])
    print()

print("Binding to socket...")
s = socket(AF_PACKET, SOCK_RAW)
s.setblocking(0)
s.bind((interface, protocol))

print("Receiving packets...")
ready = select([s], [], [], 5)
if ready[0]:
    obj = s.recv(1024)
    print("Printing object...")
    print(obj)
else:
    print("Timed out")

