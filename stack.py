""" Stack"""

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peep(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)



stack = Stack()
#Push
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
#Pop
print pop()
#Peep
print peep()
# Size of the stack
print size()
