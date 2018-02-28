""" Stack """

class Stack(object):

    def __init__(self,size):
        self.stack = []
        self.top = -1
        self.size = size


    def push(self,val):
        if self.is_full():
            print "Stack overflow"
            return

        self.stack.append(val)
        self.top += 1


    def pop(self):
        if self.is_empty():
            print "Stack underflow"
            return
        else:
            self.top -= 1
            return self.stack.pop()


    def peek(self):
        return self.stack[self.top]


    def ssize(self):
        return (self.top + 1)


    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


    def is_full(self):
        if (self.top + 1) == self.size:
            return True
        else:
            return False




#                                     ### Testcases ###
# stack = Stack(4)
# #Push
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# print stack.stack
# #Pop
# print stack.pop()
# #Peek
# print stack.peek()
# #Size of the stack
# print stack.ssize()
# #Resulting stack - [5,6,7]
# print stack.stack
