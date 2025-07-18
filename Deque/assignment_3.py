#this assignment is based on the concept of Doubly linked List..!

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next


class Deque:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count_Item = 0

    def is_empty(self):
        return self.count_Item == 0
    
    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.count_Item += 1

    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count_Item += 1

    def delete_front(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front =None
                self.rear = None
            else:
                self.front =self.front.next
                self.front.prev = None
            self.count_Item -= 1
        else:
            raise IndexError("Deque is empty!!!")
        
    def delete_rear(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front =None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next =None
            self.count_Item -= 1
        else:
            raise IndexError("Deque is empty!!!")
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is empty!!!")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item           
        else:
            raise IndexError("Deque is empty!!!")
            

    def size(self):
        return self.count_Item
    
    def printing(self):
        if not self.is_empty():
            temp = self.front
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
    

d1 =Deque()
d1.insert_front(20)
d1.insert_front(10)
d1.insert_rear(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.printing()
print()
d1.delete_front()
d1.delete_rear()
d1.printing()
print()
print(f"the front element is : {d1.get_front()}")
print(f"the rear element is : {d1.get_rear()}")
print(d1.size())

