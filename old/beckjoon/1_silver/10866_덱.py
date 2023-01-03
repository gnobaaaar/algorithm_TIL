import sys

class Deque:
    def __init__(self):
        self.deque = []

    def array_return(self):
        return self.deque

    def push_front(self, num):
        self.deque.insert(0,num)

    def push_back(self, num):
        self.deque.insert(len(self.deque), num)

    def pop_front(self):
        tmp_value = 0
        if self.deque:
            tmp_value = self.deque[0]
            self.deque = self.deque[1:]
            return tmp_value
        else:
            return -1

    def pop_back(self):
        tmp_value = 0
        if self.deque:
            tmp_value = self.deque[-1]
            self.deque = self.deque[:len(self.deque)-1]
            return tmp_value
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.deque:
            return 0
        else:
            return 1

    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1

deque = Deque()

for i in range(int(input())):
    a = sys.stdin.readline().split()
    if a[0] == 'push_back':
        deque.push_back(int(a[1]))
    elif a[0] == 'push_front':
        deque.push_front(int(a[1]))
    elif a[0] == 'front':
        print(deque.front())
    elif a[0] == 'back':
        print(deque.back())
    elif a[0] == 'size':
        print(deque.size())
    elif a[0] == 'empty':
        print(deque.empty())
    elif a[0] == 'pop_front':
        print(deque.pop_front())
    elif a[0] == 'pop_back':
        print(deque.pop_back())
    elif a[0] == 'array_return':
        print(deque.array_return())