# 3. I'm using hosts.txt to show you hosts' IPs:

import sys

hosts = {}

with open('hosts') as f:
    for line in f:
        key, value = line.strip().split("=")
        hosts[key] = value

print(sys. argv)
print(hosts)

for place in sys.argv[1:]:
    if place in hosts:
        print(f"host {place} has IP Address {hosts[place]}")
    else:
        print(f"no IP address found for {place}")