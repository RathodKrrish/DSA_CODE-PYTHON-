#this is Deque data structure. This code is emplement with using list method of python.

class Deque:
    def __init__(self):
        self.mylist = []
        self.itemCount = 0

    def is_Empty(self):
        return self.itemCount == 0
    
    def size(self):
        return self.itemCount
    
    def insert_front(self,data):
        self.mylist.insert(0,data)
        self.itemCount += 1

    def insert_rear(self,data):
        self.mylist.append(data)
        self.itemCount += 1

    def delete_front(self):
        if not self.is_Empty():
            del self.mylist[0]
            self.itemCount -= 1
        else:
            raise IndexError("Deque is Empty!")
        
    def delete_rear(self):
        if not self.is_Empty():
            self.mylist.pop()
            self.itemCount -= 1
        else:
            raise IndexError("Deque is Empty!")
        
    def get_front(self):
        if not self.is_Empty():
            return self.mylist[0]
        else:
            raise IndexError("Deque is Empty!")
        
    def get_last(self):
        if not self.is_Empty():
            return self.mylist[-1]
        else:
            raise IndexError("Deque is Empty!")
        

d1 = Deque()
d1.insert_front(10)
d1.insert_rear(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.insert_rear(60)
print(d1.mylist)
print(f"Before Deletion The Size Of Deque Is : {d1.size()}.")
d1.delete_front()
d1.delete_rear()
d1.delete_rear()
print(d1.mylist)
print(f"After Deletion The Size Of Deque Is : {d1.size()}.")
print(f"The First Element Of Deque Is : {d1.get_front()}")
print(f"The last Element Of Deque Is : {d1.get_last()}")
