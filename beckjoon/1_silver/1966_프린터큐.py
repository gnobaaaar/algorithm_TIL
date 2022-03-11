for i in range(int(input())):
    n, index = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    tmp = index
    count = 1

    while len(arr):
        if arr[0] == max(arr):
            if tmp == 0:
                print(count)
                break
            else:
                arr.pop(0)
                tmp -= 1
                count += 1
        else:
            if tmp == 0:
                arr.append(arr.pop(0))
                tmp = len(arr) -1
            else:
                arr.append(arr.pop(0))
                tmp -= 1

