from pyroute2 import IPRoute

# create RTNL socket
ipr = IPRoute()

# subscribe to broadcast messages
ipr.bind()

# wait for data (do not parse it)
data = ipr.recv(65535)

# parse received data
messages = ipr.marshal.parse(data)

# shortcut: recv() + parse()
#
# (under the hood is much more, but for
# simplicity it's enough to say so)
#
messages = ipr.get()
