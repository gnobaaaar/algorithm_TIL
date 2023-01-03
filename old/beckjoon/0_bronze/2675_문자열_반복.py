import sys

for j in range(int(input())):
    string = sys.stdin.readline().split()
    for i in list(string[1]):
        print(i * int(string[0]), end="")
    print()