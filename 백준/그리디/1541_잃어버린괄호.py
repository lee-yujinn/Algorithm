import sys
input = sys.stdin.readline

n = str(input()).split("-")

def findmin():
    if len(n) == 1:
        p = n[0].split("+")
        return sum(list(map(int,p)))
    else:
        m, s = 0, 0
        if "+" in n[0]:
            s = sum(list(map(int,n[0].split("+"))))
        else:
            s = int(n[0])
        for v in n[1:]:
            if "+" in v:
                l = v.split("+")
                m += sum(list(map(int,l)))
            else:
                m += int(v)
        return s - m

print(findmin())
