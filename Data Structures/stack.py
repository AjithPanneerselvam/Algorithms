""" Stack """

class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        self.top -= 1
        return self.stack.pop()

    def peep(self):
        return self.stack[self.top]

    def size(self):
        return self.top + 1


#stack = Stack()
##Push
#stack.push(5)
#stack.push(6)
#stack.push(7)
#stack.push(8)
#print stack.stack
##Pop
#print stack.pop()
##Peep
#print stack.peep()
##Size of the stack
#print stack.size()
##Resulting stack - [5,6,7]
#print stack.stack
