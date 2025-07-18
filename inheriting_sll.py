from demo_sll import *
class Stack(sll):
    def __init__(self):
        super().__init__()  #this is compulsory to call parent class init method if we dont it willnot make self object and we face the error
        # this is the way to call parent class method from child class when the both class name is same in parent and child class
        self.item_count = 0


    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_first(data)
        self.item_count +=1
        

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
            

    def peek(self):
        if not self.is_empty():
            return self.start.item
        
    def size(self):
        return self.item_count
    
s1=Stack()
s1.push(10)        
s1.push(20)        
s1.push(30)        
print(f"The top element is :{s1.peek()}")
s1.pop()
print(f"The top element is :{s1.peek()}")
s1.size()

    

