# THis assignment is emplement with the help of list inheritance

class Deque(list):
    def __init__(self):
        self.itemCount = 0

    def is_empty(self):
        return self.itemCount == 0
    
    def size(self):
        return self.itemCount
    
    def insert_front(self,data):
        self.insert(0,data)
        self.itemCount += 1

    def insert_rear(self,data):
        self.append(data)
        self.itemCount += 1

    def delete_front(self):
        if not self.is_empty():    
            del self[0]
            self.itemCount -= 1
        else:
            raise IndexError("Deque is empty!")
        
    def delete_rear(self):
        if not self.is_empty():
            self.pop()
            self.itemCount -= 1
        else:
            raise IndexError("Deque is empty!")
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Deque is empty!")
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Deque is empty!")
        



d1 = Deque()
d1.insert_front(10)
d1.insert_rear(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.insert_rear(60)
print(d1)
print(f"Before Deletion The Size Of Deque Is : {d1.size()}.")
d1.delete_front()
d1.delete_rear()
d1.delete_rear()
print(d1)
print(f"After Deletion The Size Of Deque Is : {d1.size()}.")
print(f"The First Element Of Deque Is : {d1.get_front()}")
print(f"The last Element Of Deque Is : {d1.get_rear()}")
