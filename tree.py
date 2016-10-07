#An implementation for a tree with left child/right sibling representation
# A tree node that has a value , pointer to left child and pointer to right sibling 
class Node:
    def __init__(self, value):
        self.leftchild = None 
        self.rightsib = None  
        self.value = value  
 # A tree class       
class Tree:
    def __init__(self):    #Constructor
        self.root = None 
# Function to look for a target value in the Tree
#Returns the node
    def  find(self, target):
        if(self.root is not None):
            return self.findpreorder(target, self.root) #calls the recursive function 
        else:
            return None   # Root of the tree is None    


    def findpreorder(self, target, node):
        x=y= None
        if target == node.value:
            return node
        if node.leftchild:
             x = self.findpreorder(target,node.leftchild)
        if node.rightsib:
             y = self.findpreorder(target,node.rightsib)
        if x is not None: 
            return x 
        elif y is not None:
            return y 
#Function to inser a node child with parent
    def insert(self, node,parent):
        if self.root == None:
            self.root = node
        else:   
            if parent.leftchild is None:  #Add as first (left) child
                parent.leftchild = node
            else:  
                parent = parent.leftchild
                while parent.rightsib is not  None:  #Traverse through next children until you reach the last one
                    parent = parent.rightsib  
                parent.rightsib = node    


 #Function to delete a node with parent    
    def delete(self,node,parent=None):
        if node == None:
            return
        if self.root == node:
            if self.root.leftchild:  
                self.root= None         #lose the tree
        else:
            if node == parent.leftchild:
                parent.leftchild = parent.leftchild.rightsib #remove first child from the tree
            else: 
                parent = parent.leftchild
                while parent.rightsib  != node:
                    parent= parent.rightsib
                parent.rightsib = parent.rightsib.rightsib   #remove right sibling from the tree 
                                                                #lose all its subtree
                
                   
            
def main():
    tree= Tree()
    n1= Node('A')
    tree.insert(n1,None) #root
    n2=Node('B')
    tree.insert(n2,n1) #n2 is left(first) child of n1
    n3= Node('C') 
    n4 = Node('D')
    tree.insert(n4,n2) #n4 first child of n2
    tree.insert(n3,n2) #n3 second child of n2
    n5= Node('E')
    n6= Node('F')
    n7= Node('G')
    tree.insert(n5,n1) #n2 is second child of n1
    tree.insert(n6,n1) #n2 is third child of n1
    tree.insert(n7,n1) #n2 is last child of n1
    print tree.find('F').value
    print tree.find('G').value
    tree.delete(n7,n1)
    print tree.find('E').value
    


if __name__ == "__main__":
    main()       