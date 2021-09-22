import sys

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        dequeue_num = None
        if self.queue:
            dequeue_num = self.queue[0]
            self.queue = self.queue[1:]
            return dequeue_num
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1

my_queue = Queue()
n = int(input())
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        my_queue.push(int(a[1]))
    elif a[0] == 'pop':
        print(my_queue.pop())
    elif a[0] == 'size':
        print(my_queue.size())
    elif a[0] == 'empty':
        print(my_queue.empty())
    elif a[0] == 'front':
        print(my_queue.front())
    elif a[0] == 'back':
        print(my_queue.back())
