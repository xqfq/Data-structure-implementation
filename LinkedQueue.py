class Node:
    def __init__(self):
        # consists of an item and a reference to the next node
        self.item = None
        self.next = None
class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0
    def isEmpty(self):
        return self.len == 0
    def size(self):
        return self.len
    def enqueue(self,item):
        newLast = Node()
        newLast.item = item
        oldLast = self.last
        self.last = newLast
        self.len += 1
        if self.first == None:
            self.first = self.last
        else:
            oldLast.next = self.last
    def dequeue(self):
        oldFirst = self.first
        if self.len != 0:
            newFirst = oldFirst.next
            self.first = newFirst
            self.len -= 1
            return oldFirst.item
        else:
            print('The stack is empty.')
            pass
