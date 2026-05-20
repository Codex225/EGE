import ipaddress
from ipaddress import *

ip1 = ip_address("200.154.190.12")
ip2 = ip_address("200.154.184.0")
for mask in range(1, 33):
    net = ip_network(f"200.154.190.12/{mask}", 0)
    if ip1 in net and ip2 in net and net[0] < ip1 < net[-1] and  net[0] < ip2 < net[-1]:
        print(mask)