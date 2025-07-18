class stack(list):

    def is_empty(self):
        return len(self) == 0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        if self == 0:
            raise IndexError("list is empty")
        else:
            return super().pop()
        
    def peek(self):
        if self == 0:
            raise IndexError("list is empty")
        else:
            return self[-1]
        
    def size(self):
        return len(self)
    
    def insert(self,index,data): #its a builtin function of list!
        raise AttributeError("'INSERT' ATTRIBUTE ARE NOT AVAILABLE IN 'STACK' ")
    
s1=stack()
s1.push(15)
s1.push(20)
# s1.insert(0,10)
s1.push(25)
s1.push(30)
print(s1)
s1.pop()
s1.pop()

print(f"Peeking the element is : {s1.peek()}")
print("Remaining list is .......")
print(s1)
