s = str(input())
stack = []

def right(s):
    stack = []
    for v in s:
        if v == '(' or v == '[':
            stack.append(v)
        elif v == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(v)
        elif v == ']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(v)
    if stack:
        return False
    return True

def result(s):
    for v in s:
        if v == '(' or v == '[':
            stack.append(v)
        elif v == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                value = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = value * 2
                        break
                    else:
                        value += stack.pop()
        elif v == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                value = 0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == '[':
                        stack[-1] = value * 3
                        break
                    else:
                        value += stack.pop()
if right(s):
    result(s)
    print(sum(stack))
else:
    print(0)
