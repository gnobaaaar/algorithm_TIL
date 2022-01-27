for i in range(int(input())):
    num = input().replace(',', ' ')
    print(sum(map(int, num.split())))
