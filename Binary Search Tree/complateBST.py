class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
# 1.this is for insertion of Node in binary search tree with using recursion:
    def insert(self,data):
        self.root=self.rinsert(self.root,data)

    def rinsert(self,root,data):
        if root == None:
            return Node(data)
        if data < root.item:
            root.left=self.rinsert(root.left,data)
        elif data > root.item:
            root.right=self.rinsert(root.right,data)
        return root
    


# 2.this is for searching of Node in binary search tree with using recursion:
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root == None or root.item == data:
            return root 
        # here we return root instead of None because if root is None it will return root and in starting we initialize root=None in BST class.
        # so if the data is === to search it will give root data as to return root but if its None it will pass None as value.
        if data < root.item:
            return self.rsearch(root.left,data)
        elif data > root.item:
            return self.rsearch(root.right,data)
        


# 3.this is for inorder traversing  of Node in binary search tree with using recursion:

    def inorder(self):
            result=[]
            self.rinorder(self.root,result)
            return result
    def rinorder(self,root,result):
        if root != None:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)

 
# 4.this is for preorder traversing  of Node in binary search tree with using recursion:   
    def preorder(self):
            result=[]
            self.rpreorder(self.root,result)
            return result
    def rpreorder(self,root,result):
        if root != None:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

 
# 4.this is for preorder traversing  of Node in binary search tree with using recursion:   
    def postorder(self):
            result=[]
            self.rpostorder(self.root,result)
            return result
    def rpostorder(self,root,result):
        if root != None:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)

# 5.this is for deletion of Node in binary search tree with using recursion:  
# if we want to delete the node we have to find (MINIMUM-MAXIMUM)Values first so we can use (SUCCESSOR-PREDECESSOR) 
# and delete the Node even if he contain two child class's.
 
    def min_value(self,temp):
        current =temp
        while current.left != None:
            current =current.left
        return current.item
    
    def max_value(self,temp):
        current=temp
        while current.right != None:
            current=current.right
        return current.item
    # Now the main function of deletion is written below.

    def delete(self,data):
        self.root =self.rdelete(self.root,data)
         
    def rdelete(self,root,data):
        if root == None:
            return root
        if data < root.item:
            root.left=self.rdelete(root.left,data)
            return root
        elif data > root.item:
            root.right=self.rdelete(root.right,data)
        else:  #when we reached at the root == data now is to delete Node
            # this both conditions are occure when the NOde contains only one child.
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
        # this condition will occure when the NOde contains Two childs.
            # this is SUCCESSOR
            root.item=self.min_value(root.right)  
            root.right=self.rdelete(root.right,root.item)
            
            # this is predecessor
        #----> root.item=self.max_value(root.left) 
              # self.rdelete(root.right,root.item)

        return root
        

# 6.this is for size Fubction of binary search tree .:

    def size(self):
        return len(self.inorder())
    




#main function code part from where all the function will called.

bst = BST()
value=[50, 30, 70, 20, 40, 60, 80]
print(f"the Values will be  insert in tree is  :{value} ")

# Insert values
for i in value:
    bst.insert(i)
print("The value is inserted succesfully.")
# Traversals
print("Inorder Traversal:", bst.inorder())  # Sorted order output
print("Preorder Traversal:", bst.preorder())  
print("Postorder Traversal:", bst.postorder())

# Search values
print("Searching (40):", "Found" if bst.search(40) else "Not Found")
print("Searching (100):", "Found" if bst.search(100) else "Not Found")

# Delete node
bst.delete(30)
print("Inorder after deleting 30:", bst.inorder())

# Tree size
print("Tree Size:", bst.size())

    