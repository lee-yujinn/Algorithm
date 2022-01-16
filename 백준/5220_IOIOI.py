import sys
input = sys.stdin.readline

n, m, s = int(input()), int(input()), str(input())
count = 0
i, p = 0, 0

while i < m-1:
    if s[i:i+3] == 'IOI':
        p += 1
        if p == n:
            count += 1
            p -= 1
        i +=1
    else:
        p = 0
    i += 1

print(count)

# 50점 
# import sys
# input = sys.stdin.readline
# 
# n, m, s = int(input()), int(input()), str(input())
# c = ""
# count = 0
# 
# for _ in range(n):
#     c += "IO"
# c += "I"
# 
# for i, v in enumerate(s):
#     if v == "I" and s[i:i+(n*2+1)] == c:
#         count += 1
# 
# print(count)
