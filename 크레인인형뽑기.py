def solution(board, moves):
    answer = 0
    temp = []
    for i in range(0,len(moves)):
        for j in range (0,len(board[0])):
            if board[j][moves[i]-1] != 0:
                temp.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                if len(temp) > 1 and temp[-1] == temp[-2]:
                    answer = answer + 1
                    del temp[-2]
                    del temp[-1]
                break
    return answer* 2

