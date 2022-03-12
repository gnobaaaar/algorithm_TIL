# 신병받아라 정렬 알고리즘
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

for i in range(1, len(numbers)):
    target = numbers[i]
    j = i-1
    while j>=0 and numbers[j] > target:
        numbers[j+1] = numbers[j]
        j -= 1
    numbers[j+1] = target

print(numbers)