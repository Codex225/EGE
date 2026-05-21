from ipaddress import *

for a in range(0, 256):
    ip0 = ip_address(f"217.109.{a}.94")
    net = ip_network(f"{ip0}/255.255.254.0", 0)
    if ip0 in net.hosts():
        if all(f"{int(adr):032b}"[:16].count("0") <= f"{int(adr):032b}"[16:].count("0") for adr in net):
            print(a)