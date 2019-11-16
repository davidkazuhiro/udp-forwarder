from socket import socket, AF_PACKET, SOCK_RAW
from netifaces import interfaces, ifaddresses

for interface in interfaces():
    print(interface)
    print(ifaddresses(interface))
    print()

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("eth0", 0))

obj = s.recv(4096)

print(obj)
