N = int(input())

three = 0
five = N // 5
rest = N % 5

if rest != 0:
    for i in range(five, -1, -1):
        if rest % 3 == 0:
            three = rest // 3
            break
        five -= 1
        rest += 5

result = five + three

if result < 1:
    result = -1
print(result)
