from socket import socket, AF_PACKET, SOCK_RAW, getprotobyname
from netifaces import interfaces, ifaddresses

interface = "eth0"
protocol = getprotobyname('udp')


print("Printing Interfaces...")
for interface in interfaces():
    print(interface)
    for entry in ifaddresses(interface):
        print(ifaddresses(interface)[entry][0]['addr'])
    print()

print("Binding to socket...")
s = socket(AF_PACKET, SOCK_RAW)
s.bind((interface, protocol))

print("Receiving packets...")
obj = s.recv(1024)

print("Printing object...")
print(obj)
