a, b, c = map(int, input().split())

try:
    n = int(a / (c-b))
except ZeroDivisionError:
    n = -1

if n < 0 :
    print(-1)
else:
    print(n+1)