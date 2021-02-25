t = int(input())

for i in range(t+1):
    k = int(input())
    d = [0]*(k+1)

    d[1] = 1
    d[2] = 2
    d[3] = 4
    
    for j in range(4,k+1):
        d[j] = d[j-1] + d[j-2] + d[j-3]

print(d[k])
