from demo_sll import *

class Stack:
    def __init__(self):
        self.mylist=sll()
        self.itemcount = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_first(data)
        self.itemcount +1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.itemcount -1
        
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item

    def size(self):
        return self.itemcount


s1=Stack()
s1.push(10)        
s1.push(20)        
s1.push(30)        
print(f"The top element is :{s1.peek()}")
s1.pop()
print(f"The top element is :{s1.peek()}")
s1.size()


    