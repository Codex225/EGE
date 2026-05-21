from ipaddress import *
q = 0
ip = ip_address("175.122.80.13")
net_ip = ip_address("175.122.80.0")
for mask in range(16, 33):
    net = ip_network(f"{ip}/{mask}", 0)
    if ip in net and net[0] < ip < net[-1] and len(list(net.hosts())) >= 28 and net.network_address == net_ip:
        q += 1
print(q)