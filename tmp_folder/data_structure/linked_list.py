# linked list class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# singly linked list 선언
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
