from ipaddress import *
ip = ip_address("123.222.111.192")
mask = "255.255.255.248"

def pr(ip):
    s = str(ip).split(".")
    print(s)
    if (bin(int(s[-1]))[2:]).count("1") % 3 !=0 :
        return 1
    return 0

q = 0
for ips in ip_network(f"{ip}/{mask}", 0):
    print(ips)
    if pr(ips):
        q += 1
print(q)
