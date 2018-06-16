class Stack:
    '''
    An expandable ordered data structure where the addition
    and the removal of items takes place at the top
    '''
    def __init__(self,cap):
        self.cap = cap
        self.stackList = [None] * cap
        self.stackLen = 0
    def __repr__(self):
        return str(self.stackList)
    def push(self,item):
        '''
        insert an item
        '''
        if self.stackLen < self.cap:
            # add item when the stack is not full
            self.stackList[self.stackLen] = item
            self.stackLen += 1
        else:
            # double the stack when full
            self.cap = self.cap * 2
            self.stackList_new =  [None] * self.cap
            for i in range(self.stackLen):
                self.stackList_new[i] = self.stackList[i]
            self.stackList_new[self.stackLen] = item
            self.stackLen += 1
            self.stackList = self.stackList_new
    def pop(self):
        '''
        deletes and returns the last inserted item
        '''
        self.stackLen -= 1
        last=self.stackList[self.stackLen]
        self.stackList[self.stackLen]=None
        return last
    def size(self):
        '''
        returns the size of the stack
        '''
        return self.stackLen
    def isEmpty(self):
        '''
        checks whether the stack is empty
        '''
        return self.stackLen == 0
