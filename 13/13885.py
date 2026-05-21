from ipaddress import *

ip = ip_address("238.51.1.202")

for mask in range(16, 25):
    net = ip_network(f"{ip}/{mask}", 0)
    if ip in net.hosts():
          if all(f"{int(address):032b}"[:16].count("1") >= f"{int(address):032b}"[16:].count("1") for address in net):
            print(net.netmask)
            break
