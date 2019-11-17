from netifaces import interfaces, ifaddresses
from select import select
from socket import socket, AF_PACKET, SOCK_RAW, getprotobyname, ntohs

interface = "eth0"
protocol = getprotobyname('udp')

print("\nPrinting Interfaces...")
for interface in interfaces():
    print(interface)
    for entry in ifaddresses(interface):
        print(ifaddresses(interface)[entry][0]['addr'])
    print()

print("Binding to socket...")
s = socket(AF_PACKET, SOCK_RAW, ntohs(3))

print("Receiving packets...")
while True:
    raw_data, addr = s.recvfrom(65535)
    print(raw_data, addr)
