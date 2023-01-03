for _ in range(int(input())):
    a = list(map(str, input().split()))
    for i in a:
        for j in i[::-1]:
            print(j, end='')
        print(' ', end='')
    print()