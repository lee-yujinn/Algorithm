num = int(input())
rope = []
rope2 = []

for i in range(num):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(num):
    rope2.append(rope[i]*(i+1))
rope2.sort()

print(rope2[-1])
