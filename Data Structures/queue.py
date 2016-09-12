""" Queue """


# C version of queue
class Queue(object):
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self,val):
        if self.is_empty():
            self.front += 1
            self.rear += 1
        else:
            self.rear += 1
            self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return "Underflow"

        elif self.front  == self.rear:
            temp = self.fornt
            self.front = self.rear = -1
            return self.queue[temp]

        else:
            self.front += 1
            return self.queue[self.front ]


    def peek(self):
        if self.is_empty():
            return "Underflow"
        else:
            print "rear",self.rear
            return self.queue[self.front]

    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False

    def size(self):
        if self.is_empty():
            return 0
        else:
            return (self.rear - self.front + 1)




#Python version of Queue
from collections import deque

class PyQueue(object):
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def is_empty(self):
        return not(len(self.queue))

    def size(self):
        return len(self.queue)



#queue = Queue()
#pyqueue = PyQueue()
#pyqueue.is_empty()
#pyqueue.enqueue(5)
#pyqueue.enqueue(6)
#pyqueue.enqueue(7)
#pyqueue.enqueue(8)
#print pyqueue.dequeue()
#print pyqueue.peek()
#print pyqueue.size()
#print pyqueue.queue

# queue = Queue()
# queue.is_empty()
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# print queue.dequeue()
# print queue.peek()
# print queue.size()
# print queue.queue
