def solution(s, n):
    result = ""
    for i in range(len(s)):
        if s[i] != " ":
            if s[i].isupper(): #대문자
                if ord(s[i]) + n > 90:
                    result += chr(ord(s[i]) + n%26 - 26)
                else:
                    result += chr(ord(s[i]) + n%26)
            else: #소문자
                if ord(s[i]) + n > 122:
                    result += chr(ord(s[i]) + n%26 - 26)
                else:
                    result += chr(ord(s[i]) + n%26)
        else:
            result += " "
    return result
