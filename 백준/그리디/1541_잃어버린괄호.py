import sys
input = sys.stdin.readline

n = str(input()).split("-")

def findmin():
    if len(n) == 1:
        p = n[0].split("+")
        return sum(list(map(int,p)))
    else:
        m, s = 0, sum(list(map(int,n[0].split("+"))))
        for v in n[1:]:
            m += sum(list(map(int,v.split("+"))))
        return s - m

print(findmin())
