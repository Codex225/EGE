from ipaddress import *
q = 0
ip_a = ip_address("108.133.75.64")
for mask in range(1, 33):
    net = ip_network(f"108.133.75.91/{mask}", 0)
    if ip_a == net.network_address:
        print(mask)
q = 0
net = ip_network("108.133.75.64/26", 0)
for host in net:
    q += 1
print(q)