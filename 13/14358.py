from ipaddress import *

ip = ip_address("192.168.32.64")
q = 0
net = ip_network("192.168.32.64/255.255.255.192")
for adr in net:
    adr2 = f"{int(adr):032b}"
    if adr2[-3:] == "101":
        q += 1
print(q)