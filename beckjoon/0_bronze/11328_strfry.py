import sys

for i in range(int(input())):
    # a, b = map(str, input().split())
    a, b = sys.stdin.readline().rstrip().split(' ')
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    # 문자열로 만드는 팁

    if a == b:
        print('Possible')
    else:
        print('Impossible')