array = [[0 for col in range(2)] for row in range(6)]
a,b = map(int, input().split())
cnt = 0

for i in range(a):
    gender, grade = map(int, input().split())
    array[grade-1][gender] += 1

for i in range(6):
    for j in range(2):
        if array[i][j] % b == 0:
            cnt += (array[i][j] // b)
        else:
            cnt += (array[i][j] // b) + 1

# for i in array:
#     for j in i:
#         cnt += math.ceil(j/b)

print(cnt)