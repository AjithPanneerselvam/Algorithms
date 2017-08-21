"""
Implementation of a singly linked list
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.length = 0


    def length(self):
        return self.length


    def insertBeginning(self,data):
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node
        self.length += 1
        return self.head


    def insertEnd(self,data):
        temp = self.head
        node = Node()
        node.data = data
        node.next = None

        while temp.next != None:
            temp = temp.next

        temp.next = node
        self.length += 1
        return self.head


    def insertPosition(self, position, data):
        node = Node()
        node.data = data

        i = 1
        temp = self.head
        while(i < position):
            previous = temp
            temp = temp.next
            i += 1

        node.next = temp
        previous.next = node
        self.length += 1
        return self.head


    def deleteBeginning(self):
        if self.head == None:
            return

        nodeDel = self.head
        self.head = self.head.next
        del(nodeDel)
        self.length -= 1
        return self.head


    def deleteEnd(self):
        if self.head == None:
            return
        if self.length == 1:
            self.head = None
            self.length -=1
            return

        temp = self.head
        while temp.next != None:
            previous = temp
            temp = temp.next

        previous.next = None
        del(temp)
        self.length -= 1
        return self.head


    def deletePosition(self,position):
        if self.head == None:
            return
        if position == 1:
            self.head = None
            return self.head

        temp = self.head
        i = 1

        while(i <= position - 2):
            temp = temp.next
            i += 1

        nodeDel = temp.next
        temp.next = nodeDel.next
        del(nodeDel)
        self.length -= 1
        return self.head


    def display(self):
        if self.head == None:
            return

        temp = self.head
        while temp != None:
            print ("{} -> ".format(temp.data), end = ' ')
            temp = temp.next

        print ("NULL")


    def displayListLength(self):
        print (self.length)
                                    ### Testcases ###

# listObj = List()
# listObj.insertBeginning(1)
# listObj.insertEnd(3)
# listObj.insertEnd(4)
# listObj.insertEnd(5)
# listObj.display()
# listObj.length
# listObj.displayListLength()
# listObj.insertPosition(2, 2)
# listObj.display()
# listObj.deletePosition(3)
# listObj.display()
# listObj.deleteEnd()
# listObj.deleteBeginning()
# listObj.display()
