def solution(number, k):
    answer = ''
    result = []
    
    for v in number:
        if len(result)>0 and k > 0:
            for _ in range(len(result)):
                if result[-1] < v and k > 0:
                    result.pop()
                    k -= 1
                else: break
        result.append(v)
    while k > 0:
        result.pop()
        k-=1
    # answer = "".join(result[0:-k]) if k > 0 else "".join(result)
    return "".join(result)
