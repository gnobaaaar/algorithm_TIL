def group_word_checker(a):
    b = []
    for i in range(len(a)):
        if i == 0:
            b.append(a[i])
            # print(b)
        else:
            if a[i] == a[i-1]:
                pass
            else:
                if a[i] not in b:
                    b.append(a[i])
                    # print(b)
                else:
                    # print(a[i])
                    # print('중복됩니다')
                    return 0
    return 1

cnt = 0
for i in range(int(input())):
    cnt += group_word_checker(input())

print(cnt)
