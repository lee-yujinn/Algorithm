word = str(input())
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for v in a:
    if v in word:
        cnt += word.count(v)
        word = word.replace(v,'0')

print(cnt+len(word)-word.count('0'))
