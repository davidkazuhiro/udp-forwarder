How to test

In shell 1
```
vagrant up
vagrant ssh
docker run -it quay.io/dksh/udp-forwarder
```

In shell 2
```
vagrant ssh
nc -u ${IP_ADDRESS} 53 < /dev/random
```
