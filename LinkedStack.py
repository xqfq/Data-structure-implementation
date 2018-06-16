class Node:
    def __init__(self):
        # consists of an item and a reference to the next node
        self.item = None
        self.next = None
class LinkedStack:
    def __init__(self):
        self.first = None
        self.len = 0
    def isEmpty(self):
        return self.len == 0
    def size(self):
        return self.len
    def push(self, item):
        # push by updating the first node and the len attribute
        oldFirst = self.first
        newFirst = Node()
        newFirst.item = item
        newFirst.next = oldFirst
        self.first = newFirst
        self.len += 1
    def pop(self):
        # pop by updating the first node and the len attribute
        oldFirst = self.first
        if self.len != 0:
            newFirst = oldFirst.next
            self.first = newFirst
            self.len -= 1
            return oldFirst.item
        else:
            print('The stack is empty.')
            pass
