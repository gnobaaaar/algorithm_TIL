a, b = map(str, input().split())

if int(a[::-1]) > int(b[::-1]):
    print(int(a[::-1]))
elif int(a[::-1]) < int(b[::-1]):
    print(int(b[::-1]))