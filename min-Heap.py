class minHeap: 
    def __init__(self): 
        self.heapList = [0] 
        self.currentSize = 0 

    def __repr__(self): 
        return self.heapList

    def percUp(self,i): 
        ''' 
        takes an index representing the element in concern 
        returns the Heap object that is reordered by swapping the element upwards 
        ''' 
        while i // 2 > 0: 
            if self.heapList[i] < self.heapList[i // 2]: 
                tmp = self.heapList[i // 2] 
                self.heapList[i // 2] = self.heapList[i] 
                self.heapList[i] = tmp 
            i = i // 2 

    def insert(self,k): 
        ''' 
        takes an integer 
        inserts the input into the Heap object  
        returns the Heap object reordered properly 
        ''' 
        self.currentSize = self.currentSize + 1 
        self.heapList.append(k) 
        self.percUp(self.currentSize) 

    def minChild(self,i): 
        ''' 
        takes an index 
        returns the index of the smaller child of this node 
        ''' 
        if i * 2 + 1 > self.currentSize: 
        # if there does not exist a right child
            return i * 2 
        else: 
            if self.heapList[i * 2 + 1] < self.heapList[i * 2]: 
                return i * 2 + 1 
            else: 
                return i * 2  

    def percDown(self,i): 
        ''' 
        takes an index 
        returns the Heap reordered by swapping downward properly 
        ''' 
        while (i * 2) <= self.currentSize: 
            minindex = self.minChild(i) 
            if self.heapList[i] > self.heapList [minindex]: 
                temp = self.heapList[minindex] 
                self.heapList[minindex] = self.heapList[i] 
                self.heapList[i] = temp 
            i = minindex 

    def delmin(self): 
        ''' 
        deletes the minimum element of the Heap and adjusts the Heap properly 
        returns minimum element 
        ''' 
        output = self.heapList[1] 
        temp = self.heapList[self.currentSize] 
        self.heapList[self.currentSize]=output 
        self.heapList[1]=temp 
        self.heapList.pop() 
        self.currentSize -= 1 
        self.percDown(1) 
        return output 

    def buildHeap(self,k): 
        ''' 
        takes a list 
        builds a heap based on this list 
        ''' 

        i = len(k) // 2 
        self.heapList = [0] + k[:] 
        self.currentSize=len(k) 
        while (i <= self.currentSize): 
            self.percUp(i) 
            i += 1 
