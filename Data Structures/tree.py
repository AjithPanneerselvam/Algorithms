"""                        ---------Tree---------                            """


# Defining node
class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

# Operations performed on the tree
class Tree(object):
    def insert(self,root,val):
        if root == None:
            root = Node(val=val)
            return root

        if(root.val >= val):
            root.left = self.insert(root.left,val)

        elif (root.val < val):
            root.right = self.insert(root.right,val)

        return root

    def preorder(self,root):
        if root != None:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print root.val

    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print root.val
            self.inorder(root.right)



#tree = Tree()
#root = None

## Enter the number of nodes in a tree
#number_of_nodes = input()
#while(number_of_nodes):
#    val = input()
#    root = tree.insert(root,val)
#    number_of_nodes -= 1

##Traversals
#print "Preorder Traversal"
#tree.preorder(root)
#print "Postorder Traversal"
#tree.postorder(root)
#print "Inorder Traversal"
#tree.inorder(root)
