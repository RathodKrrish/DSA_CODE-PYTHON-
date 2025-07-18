class Stack:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item) == 0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")
        
    def peak(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
         return len(self.item)
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(f"the top element is :{s1.peak()}")
print(f"The removing element is :{s1.pop()}")
print(f"the top element is :{s1.peak()}")
print(f"The removing element is :{s1.pop()}")

        
    