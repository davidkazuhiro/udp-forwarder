export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y docker.io traceroute
docker pull quay.io/dksh/udp-forwarder
