import re
def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r"[^a-zA-Z0-9-_.]",'', answer)
    answer = re.sub(r'\.+', r'.', answer)
    answer = re.sub(r'^\.', r'', answer)
    if answer == "": answer = "a"
    answer = answer[:15]
    answer = re.sub(r'\.$', r'', answer)
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer
