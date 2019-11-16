How to test

In shell 1
```
vagrant up
vagrant ssh

# Run udp-forwarder
docker run -it quay.io/dksh/udp-forwarder

# Troubleshooting
tcpdump -i eth0 udp port 54
```

In shell 2
```
vagrant ssh

# Send Traffic
nc -u ${IP_ADDRESS} 54 < /dev/random
```
