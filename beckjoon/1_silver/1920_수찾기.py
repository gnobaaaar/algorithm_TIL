n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(list, target):
    min = 0
    max = len(list) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = list[mid]

        if guess == target:
            return 1
        if guess > target:
            max = mid - 1
        else:
            min = mid +1
    return 0

n_list.sort()

for i in m_list:
    print(binary_search(n_list, i))


