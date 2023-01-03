import sys

length = int(input())
array = list(map(int, sys.stdin.readline().rstrip()))
sum = 0

for i in range(length):
    sum += int(array[i])

print(sum)