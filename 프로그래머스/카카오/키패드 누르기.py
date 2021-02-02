def solution(numbers, hand):
    position = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    answer = ''
    left = '*'
    right = '#'
    left_distance = 0
    right_distance = 0
    
    for value in numbers:
        if value == 3 or value == 6 or value == 9:
            answer += 'R'
            right = str(value)
        elif value == 1 or value == 4 or value == 7:
            answer += 'L'
            left = str(value)
        else:
            #왼손 거리 구하기
            left_distance = abs(position[str(value)][0] - position[left][0]) + abs(position[str(value)][1] - position[left][1])
            #오른손 거리 구하기
            right_distance = abs(position[str(value)][0] - position[right][0]) + abs(position[str(value)][1] - position[right][1])
            
            if left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    right = str(value)
                else: 
                    answer += 'L'
                    left = str(value)
            else:
                if left_distance < right_distance:
                    answer += 'L'
                    left = str(value)
                else:
                    answer += 'R'
                    right = str(value)
    return answer
