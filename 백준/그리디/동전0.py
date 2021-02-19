num, price = map(int, input().split())
money = []
count = 0

for _ in range(num):
    money.append(int(input()))

for v in sorted(money,reverse = True):
    if price % v != price:
        count += int(price / v)
        price = price % v

print(count)
