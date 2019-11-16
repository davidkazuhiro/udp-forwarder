from python:latest
run pip install pyroute2 netifaces
copy forwarder.py .
cmd python forwarder.py
