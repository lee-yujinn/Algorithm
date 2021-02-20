num = int(input())
time = []
time = list(map(int, input().split()))
total = 0
time.sort()

for i in range(num):
    for i2 in range(i+1):
        total += time[i2]
    
print(total)
