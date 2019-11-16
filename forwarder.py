from pyroute2 import IPRoute
from netifaces import interfaces, ifaddresses

for interface in interfaces():
    print(interface)
    print(ifaddresses(interface))
    print()
 


# create RTNL socket
ipr = IPRoute()

# subscribe to broadcast messages
ipr.bind()

print("Receiving data...")

# wait for data (do not parse it)
data = ipr.recv(65535)

print("Parsing data...")

# parse received data
messages = ipr.marshal.parse(data)

print("Printing messages with ipr.marshal.parse(data)")

print(messages)

# shortcut: recv() + parse()
#
# (under the hood is much more, but for
# simplicity it's enough to say so)
#
messages = ipr.get()

print("Printing messages with ipr.get()")

print(messages)
