for i in range(int(input())):
    num, target = map(int, input().split())
    qu = list(map(int, input().split()))
    result = []
    now = target
    index = 0
    while qu:
        if now == 0 and qu[0] == max(qu):
            result.append(qu.pop(0))
            print(len(result))
            break
        elif qu[0] == max(qu):
            now -= 1
            result.append(qu.pop(0))
        elif now == 0 and qu[0] < max(qu):
            now = len(qu) - 1
            tmp = qu.pop(0)
            qu.append(tmp)
        elif qu[0] < max(qu):
            now -= 1
            tmp = qu.pop(0)
            qu.append(tmp)

