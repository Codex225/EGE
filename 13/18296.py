from ipaddress import *
ip = ip_address("222.190.122.24")
ip_net = ip_address("222.190.120.0")
n = 0
for mask in range(16, 33):
    net = ip_network(f"{ip}/{mask}", 0)
    if ip in net.hosts() and ip_net == net.network_address:
        n = max(n, net.num_addresses)
print(n - 3)