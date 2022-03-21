def solution(string, number):
    answer = ''

    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            if ord(i) + number > 90:
                answer += chr(ord(i) + number - 26)
            else:
                answer += chr(ord(i) + number)
        elif ord(i) > 96 and ord(i) <= 122:
            if ord(i) + number > 122:
                answer += chr(ord(i) + number - 26)
            else:
                answer += chr(ord(i) + number)
        else:
            answer += ' '

    return answer



# 다른사람풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)