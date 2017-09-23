"""
Implementation of PriorityQueue using Binary Heap
"""

class PriorityQueue():
    def __init__(self, listValues = []):
        self.size = 0
        self.pqueue = ['#']
        for val in listValues:
            self.pqueue.append(val)
            self.size += 1
            self.percolateUp(self.size)


    def peekMin(self):
        if self.size == 0:
            return
        return self.pqueue[1]


    def __str__(self):
        if self.size == 0:
            return
        return str(self.pqueue)


    def minChildIndex(self, index):
        if ((index * 2) + 1) <= self.size:
            if self.pqueue[(index * 2) + 1][0] < self.pqueue[index * 2][0]:
                return ((index * 2) + 1)
            elif self.pqueue[(index * 2) + 1][0] > self.pqueue[index * 2][0]:
                return (index * 2)
            else:
                # return any node, if both the children has same value
                return (index * 2)
        elif (index * 2) <= self.size:
            return (index * 2)
        else:
            # No children for the given Node
            return (-1)


    def percolateUp(self, index):
        parent = int(index / 2)
        while(parent >= 1 and self.pqueue[parent][0] > self.pqueue[index][0]):
            self.pqueue[parent][0], self.pqueue[index][0] = self.pqueue[index][0], self.pqueue[parent][0]
            self.pqueue[parent][1], self.pqueue[index][1] = self.pqueue[index][1], self.pqueue[parent][1]
            index = parent
            parent = int(parent / 2)


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            minChildIndex = self.minChildIndex(index)
            if self.pqueue[index][0] > self.pqueue[minChildIndex][0]:
                self.pqueue[index][0], self.pqueue[minChildIndex][0] = self.pqueue[minChildIndex][0], self.pqueue[index][0]
                self.pqueue[index][1], self.pqueue[minChildIndex][1] = self.pqueue[minChildIndex][1], self.pqueue[index][1]
            index = minChildIndex


    def extractMin(self):
        if self.size == 0:
            return

        self.size -= 1
        if self.size == 1:
            return self.pqueue.pop()

        minElement = self.pqueue[1]
        self.pqueue[1] = self.pqueue[-1]
        self.pqueue.pop()
        self.percolateDown(1)
        return minElement


    def decreaseKey(self, index, newValue):
        oldValue = self.pqueue[index][0]
        self.pqueue[index][0] = newValue
        if newValue < oldValue:
            self.percolateUp(index)
        elif newValue > oldValue:
            self.percolateDown(index)


    def insert(self, data):
        self.pqueue.append(data)
        self.size += 1
        self.percolateUp(self.size)


#                                       ### Testcases ###
# heapObj = PriorityQueue([[9,'a'],[5,'b'],[4,'c'],[3,'d'],[8,'e'],[7,'f'],[6,'g']])
# print(heapObj)
# heapObj.insert([1,'h'])
# print(heapObj)
# heapObj.insert([2,'i'])
# print(heapObj)
# print (heapObj.extractMin())
# print(heapObj)
# print (heapObj.peekMin())
# heapObj.decreaseKey(4,1)
# print(heapObj)
# heapObj.decreaseKey(2,11)
# print(heapObj)
