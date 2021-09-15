str = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alpha)):
    if alpha[i] in str:
        # print(alpha[i], end='')
        print(str.index(alpha[i]), end=' ')
    else:
        print(-1, end=' ')


# import string
# a = input()
# for i in string.ascii_lowercase:
#   print(a.find(i), end=' ')

# string.ascii_letters : 영어 소문자, 대문자를 모두 출력
# string.ascii_lowercase : 영어 소문자를 출
# string.digits : 십진수 0-9 출력