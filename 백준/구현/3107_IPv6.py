import sys
input = sys.stdin.readline

ip = str(input().strip()).split(":")
ipv6 = []
f = False
i = 0

for v in ip:
    l = len(v)
    if l == 4: ipv6.append(v)
    elif 0 < l < 4: ipv6.append('0' * (4-l) + v)
    else:
        if not f:
            f = True
            n = 8-(len(list(set(ip)))-1)
            for _ in range(n):
                ipv6.append('0000')

print(':'.join(ipv6))
