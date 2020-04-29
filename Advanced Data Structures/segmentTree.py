"""
Segment Tree

Build - O(n)
Query - O(log n)
Update - O(log n)

The below segement tree aims to return the minimum number in the given range (l,r).
"""

from sys import maxsize

class SegTree:
    def __init__(self, listVal):
        if len(listVal) == 0:
            raise AssertionError("Cannot build a Segment Tree with size 0!")
        nearestPowerTwo = self.nearestPowerTwo(len(listVal))

        self.STree =  [-1 for i in range(2*nearestPowerTwo - 1)]
        self.lazyTree = [0 for i in range(2*nearestPowerTwo - 1)]
        self.build(listVal, 0, 0, len(listVal) - 1)


    # Auxiliary method for building Segment Tree
    def nearestPowerTwo(self, n):
            # if n is already a power of 2
            if n and (n & n -1) == 0:
                return n

            p = 1
            while p < n:
                p = p << 1

            return p


    def build(self, listVal, nIndex, left, right):
        if left == right:
            self.STree[nIndex] = listVal[left]
            # Leaf node which is not at the last level of the tree
            if (2*nIndex + 1) < len(self.STree):
                self.STree[2*nIndex + 1] = None
                self.STree[2*nIndex + 2] = None
            return

        mid = int((left + right) / 2)
        self.build(listVal, 2*nIndex + 1, left, mid)
        self.build(listVal, 2*nIndex + 2, mid + 1, right)
        self.STree[nIndex] = min(self.STree[2*nIndex + 1], self.STree[2*nIndex + 2])


    def query(self, l, r, nIndex, start, end):
        if (start > r or end < l):
            # Return a maximum integer to ignore this node
            return maxsize

        if (start >= l and end <= r):
            return self.STree[nIndex]

        mid = int((start + end) / 2)
        left = self.query(l, r, 2*nIndex + 1, start, mid)
        right = self.query(l, r, 2*nIndex + 2, mid + 1, end)
        return min(left, right)


    ## Lazy Propagation
    def updat
    e(self, l, r, val, nIndex, start, end):
        if start > end:
            return

        if self.lazyTree[nIndex] != 0:
            self.STree[nIndex] += self.lazyTree[nIndex]
            # Internal Node
            if start != end:
                self.lazyTree[2*nIndex + 1] = self.lazyTree[nIndex]
                self.lazyTree[2*nIndex + 2] = self.lazyTree[nIndex]
            self.lazyTree[nIndex] = 0

        if start > r or end < l:
            return

        if start >= l and end <= r:
            self.STree[nIndex] += val
            if start != end:
                self.lazyTree[2*nIndex + 1] += val
                self.lazyTree[2*nIndex + 2] += val
            return

        mid = int((start + end) / 2)
        self.update(l, r, val, 2*nIndex + 1, start, mid)
        self.update(l, r, val, 2*nIndex + 2, mid + 1, end)
        self.STree[nIndex] = min(self.STree[2*nIndex + 1], self.STree[2*nIndex + 2])


    def display(self):
        print(self.STree)
        print(self.lazyTree)


### Test ###
listVal = [1, 3, 5, 7, 9, 11]
sObj = SegTree(listVal)
print(sObj.query(0, 3, 0, 0, len(listVal) - 1))
print(sObj.query(3, 5, 0, 0, len(listVal) - 1))
print(sObj.query(2, 4, 0, 0, len(listVal) - 1))
print(sObj.query(0, 5, 0, 0, len(listVal) - 1))

sObj.update(0, 2, 1, 0, 0, len(listVal) - 1)
sObj.display()
print(sObj.query(0, 2, 0, 0, len(listVal) - 1))

sObj.update(1, 3, 1, 0, 0, len(listVal) -1)
sObj.display()
print(sObj.query(3, 5, 0, 0, len(listVal) - 1))

sObj.update(3, 4, 1, 0, 0, len(listVal) -1)
sObj.display()
print(sObj.query(3, 5, 0, 0, len(listVal) - 1))

sObj.update(4, 4, 2, 0, 0, len(listVal) - 1)
sObj.display()
print(sObj.query(4, 5, 0, 0, len(listVal) - 1))
