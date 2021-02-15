num_list = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)


print(sum(num_list))

    
