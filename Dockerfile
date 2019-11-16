from python:latest
apt-get update
apt-get install -y tcpdump
run pip install pyroute2 netifaces
copy forwarder.py .
cmd python forwarder.py
