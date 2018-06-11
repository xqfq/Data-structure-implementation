class Queue:
    '''
    Expandable FIFO ADT
    '''
    def __init__(self,capacity):
        self.cap = capacity
        self.queueList = [0] * capacity
        self.head = 0
        self.tail = 0
        self.len = 0
    def size(self):
        return self.len
    def isEmpty(self):
        return self.len == 0
    def enqueue(self,item):
        if self.cap > self.len:
            self.queueList[self.tail] = item
            self.len += 1
            if self.cap > (self.tail + 1):
                self.tail += 1
            else:
                self.tail = 0
        else:
            new_cap = self.cap * 2
            new_queueList = [0] * new_cap
            for i in range(self.cap):
                new_queueList[i] = self.queueList[i]
            self.len += 1
            self.tail = self.len
            new_queueList[self.tail] = item
            self.cap = new_cap
            self.queueList = new_queueList
    def dequeue(self):
        if self.len == 0:
            Error('queue empty')
        else:
            element = self.queueList[self.head]
            self.len -= 1
            if self.cap > (self.head + 1):
                self.head += 1
            else:
                self.head = 0
            return element
    def front(self):
        if self.len == 0:
            Error('queue empty')
        else:
            return self.queueList[self.head]
    def capacity(self):
        return self.cap
