import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))

def makeMax(card):
    s = 0
    for v in card[1:]:
        s += card[0] + v
    return s

print(makeMax(sorted(card, reverse=True)))
