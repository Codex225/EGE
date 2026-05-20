from ipaddress import *
ip = ip_address("218.194.82.148")
mask = "255.255.255.192"
print(ip_network(f"{ip}/{mask}", 0)[-2])
