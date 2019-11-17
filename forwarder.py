from netifaces import interfaces, ifaddresses
from select import select
from socket import socket, AF_PACKET, SOCK_RAW, ntohs, htons
from struct import unpack

def ethernet_frame(data):
    dest_mac, src_mac, proto = unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

for interface in interfaces():
    print(interface)
    for entry in ifaddresses(interface):
        print(ifaddresses(interface)[entry][0]['addr'])
    print()

s = socket(AF_PACKET, SOCK_RAW, ntohs(3))

print("Receiving packets...")
while True:
    raw_data, addr = s.recvfrom(65535)
    dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
    print(f"Destination: {dest_mac}")
    print(f"Source: {src_mac}")
    print(f"Protocol: {eth_proto}")
    print(f"Data: {data}")
