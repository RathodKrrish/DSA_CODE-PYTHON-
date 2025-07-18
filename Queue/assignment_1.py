#this is QUEUE data structure file Using List:

class Queue:
    def __init__(self):
        self.item =[]
        self.count_Items = 0

    def is_Empty(self):
        return len(self.item) == 0
    
    def enQueue(self,data):
        self.item.append(data)
        self.count_Items += 1

    def deQueue(self):
        if not self.is_Empty():
            del self.item[0]
            self.count_Items -= 1
        
        else:
            raise IndexError("list is empty")
        
    def get_Front(self):
        if not self.is_Empty():
            return self.item[0]
        else:
            raise IndexError("list is empty")
        
    def get_Last(self):
        if not self.is_Empty():
            return self.item[-1]
        else:
            raise IndexError("list is empty")
        
    def size(self):
        return self.count_Items
    
    def insert(self,index,item):
        raise ValueError("insert Function is not Workable in Queue.")
    

Q1= Queue()
Q1.enQueue(10)
Q1.enQueue(20)
Q1.enQueue(30)
Q1.enQueue(40)
Q1.enQueue(50)
print(f"the list is : {Q1.item}")
Q1.deQueue()
Q1.deQueue()
print(f"the list is : {Q1.item}")
print(f"the size of list is : {Q1.size()}")
print(f"the first element of list is : {Q1.get_Front()}")
print(f"the last element of list is : {Q1.get_Last()}")
print(f"the size of list is : {Q1.size()}")



