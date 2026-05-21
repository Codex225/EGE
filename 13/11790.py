from ipaddress import *

ip = ip_address("152.65.245.132")

def prov(ip):
    r = str(ip).split(".")
    l2b1 = "0" * (8 - len(bin(int(r[0]))[2:])) + bin(int(r[0]))[2:]
    l2b2 = "0" * (8 - len(bin(int(r[1]))[2:])) + bin(int(r[1]))[2:]
    l2b3 = "0" * (8 - len(bin(int(r[2]))[2:])) + bin(int(r[2]))[2:]
    l2b4 = "0" * (8 - len(bin(int(r[3]))[2:])) + bin(int(r[3]))[2:]
    if (l2b1 + l2b2).count("0") >= (l2b3 + l2b4).count("0"):
        return True
    return False

for a in 0, 128, 192, 224, 240, 248, 252, 254, 255:
    net = ip_network(f"{ip}/255.255.{a}.0", 0)
    if all([prov(ips) for ips in net]):
        print(a)