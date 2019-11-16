from python:latest
run apt-get update
run apt-get install -y tcpdump
run pip install pyroute2 netifaces
copy forwarder.py .
cmd python forwarder.py
