import sys

class stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return -1

    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

    def isEmpty(self):
        if self.items:
            return 0
        else:
            return 1

    def size(self):
        return len(self.items)

my_stack = stack()

for i in range(int(input())):
    a = sys.stdin.readline().split()
    print(a)
    if a[0] == 'push':
        my_stack.push(int(a[1]))
    elif a[0] == 'top':
        print(my_stack.top())
    elif a[0] == 'size':
        print(my_stack.size())
    elif a[0] == 'empty':
        print(my_stack.isEmpty())
    elif a[0] == 'pop':
        print(my_stack.pop())