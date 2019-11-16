from socket import socket, AF_PACKET, SOCK_RAW
from netifaces import interfaces, ifaddresses

print("Printing Interfaces...")
for interface in interfaces():
    print(interface)
    print(ifaddresses(interface))
    print()

print("Binding to socket...")
s = socket(AF_PACKET, SOCK_RAW)
s.bind(("eth0", 4))

print("s.recv(4096)...")
obj = s.recv(4096)

print("Printing object...")
print(obj)
