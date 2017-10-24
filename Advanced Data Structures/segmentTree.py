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

        self.sTree = ['#'] + [-1 for i in range(2 * len(listVal) - 1)]
        self.lazyTree = ['#'] + [0 for i in range(2 * len(listVal) - 1)]
        self.build(listVal, 0, 0, len(listVal) - 1)


    def build(self, listVal, nIndex, left, right):
        if left > right:
            return

        if left == right:
            self.sTree[nIndex] = listVal[left]
            return

        mid = int((left + right) / 2)
        self.build(listVal, 2*nIndex, left, mid)
        self.build(listVal, 2*nIndex + 1, mid + 1, right)
        self.sTree[nIndex] = min(self.sTree[2*nIndex], self.sTree[2*nIndex + 1])


    def query(self, l, r, nIndex, start, end):
        if (start > end or start > r or end < start):
            # Return maximum integer to ignore this node
            return maxsize

        if (start == l and end == r):
            return self.sTree[nIndex]

        mid = int((start + end) / 2)
        left = self.query(l, r, 2*nIndex, start, mid)
        right = self.query(l, r, 2*nIndex + 1, mid + 1, end)
        return min(left, right)


    ## Lazy Propagation
    def update(self, l, r, val, nIndex, start, end):
        if left > right:
            return

        if self.lazyTree[nIndex] != 0:
            self.sTree[nIndex] += self.lazyTree[nIndex]
            # Internal Node
            if start != end:
                self.lazyTree[2*nIndex] = self.lazyTree[nIndex]
                self.lazyTree[2*nIndex + 1] = self.lazyTree[nIndex]
            self.lazyTree[nIndex] = 0

        if start > r or end < l:
            return

        if start == l and end == r:
            self.sTree[nIndex] += self.lazyTree[nIndex]
            if start != low:
                self.lazyTree[2*nIndex] += val
                self.lazyTree[2*nIndex + 1] += val

        mid = int((start + end) / 2)
        self.update(l, r, val, 2*nIndex, start, mid)
        self.update(l, r, val, 2*nIndex + 1, mid + 1, end)
        self.sTree = min(self.sTree[2*nIndex], self.sTree[2*nIndex + 1])


#                                   ### Test ###
listVal = [1, 3, 5, 7, 9, 11]
sObj = SegTree(listVal)
print(sObj.query(0, 3, 1, 1, 6))
