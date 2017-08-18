"""
Maximum Heap
"""

class BinaryHeap:
    def __init__(self):
        self.size = 0
        # '#' represents that index 0 is invalid
        self.heap = ['#']


    def heapify(self):
        """
        This method is used to preserve the Heap property by swapping elements.
        """
        j = len(self.heap) - 1
        parent = int(j / 2)
        while(parent >= 1 and self.heap[parent] < self.heap[j]):
            self.heap[parent], self.heap[j] = self.heap[j], self.heap[parent]
            j = parent
            parent = int(parent / 2)


    def insert(self, data):
        self.heap.append(data)
        self.size = self.size + 1
        self.heapify()


    def maxChildIndex(self, index):
        if ((index * 2) + 1) <= self.size:
            if self.heap[(index * 2) + 1] > self.heap[index * 2]:
                return ((index * 2) + 1)
            elif self.heap[(index * 2) + 1] < self.heap[index * 2]:
                return (index * 2)
            else:
                # return any node, if both the children has same value
                return (index * 2)
        elif (index * 2) <= self.size:
            return (index * 2)
        else:
            # No children for the given Node
            return (-1)


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            maxChildIndex = self.maxChildIndex(index)
            if self.heap[index] < self.heap[maxChildIndex]:
                self.heap[index], self.heap[maxChildIndex] = self.heap[maxChildIndex], self.heap[index]
            index = maxChildIndex


    def extractMax(self):
        if self.size == 0:
            return

        self.size = self.size - 1
        if self.size == 1:
            return self.heap.pop()
        maxElement = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.percolateDown(1)
        return maxElement


    def peekMax(self):
        if self.size == 0:
            return
        return self.heap[1]


    def printHeap(self):
        if self.size == 0:
            return
        print (self.heap)


#                                 ### Testcases ###
# heapObj = BinaryHeap()
# heapObj.insert(9)
# heapObj.insert(5)
# heapObj.insert(4)
# heapObj.insert(3)
# heapObj.insert(8)
# heapObj.insert(7)
# heapObj.insert(6)
# heapObj.printHeap()
# heapObj.insert(11)
# heapObj.printHeap()
# heapObj.insert(10)
# heapObj.printHeap()
# print (heapObj.extractMax())
# heapObj.printHeap()
# print (heapObj.peekMax())
