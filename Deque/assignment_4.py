from demo_dll import *

class Deque(dll):
    def __init__(self):
        super().__init__()
        self.count_item = 0

    def is_Empty(self):
        return super().is_empty()
    
    def insert_front(self,data):
        super().insert_at_start(data)
        self.count_item += 1

    def insert_rear(self,data):
        super().insert_at_last(data)
        self.count_item += 1

    def delete_front(self):
        if not self.is_Empty():
            self.count_item -= 1
            super().delete_first()

    def delete_rear(self):
        if not self.is_Empty():
            super().delete_last()
            self.count_item -= 1

    def get_front(self):
        if not self.is_Empty():
            return self.start.item
    
    def get_rear(self):
        if not self.is_Empty():
            temp = self.start
            while temp is not None:
                if temp.next == None:
                    return temp.item
                temp = temp.next

    def size(self):
        return self.count_item
    

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