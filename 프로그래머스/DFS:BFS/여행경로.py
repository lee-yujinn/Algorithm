def solution(tickets):
    tickets.sort(reverse = True)

    d = {}
    a = []
    for i in range(len(tickets)):
        d[tickets[i][0]] = []
        
    for i in range(len(tickets)):
        d[tickets[i][0]].append(tickets[i][1])
    
    t = ['ICN']
    
    while t:
        st = t[-1]
        if st not in d or len(d[st]) == 0:
            a.append(t.pop())
        else:
            t.append(d[st].pop())

    a.reverse()
    return a
