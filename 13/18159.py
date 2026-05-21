from ipaddress import *

ip = ip_address("205.154.212.20")
ip_net = ip_address("205.154.192.0")

for mask in range(16, 25):
    net = ip_network(f"205.154.212.20/{mask}", 0)
    if ip in net.hosts() and net.network_address == ip_net:
        print(net.netmask)