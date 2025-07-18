#this Given code is based on the Concept of Linked List.


from demo_sll import *

class Queue(sll):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_Empty(self):
        return super().is_empty()

    def enQueue(self,data):
        self.insert_at_last(data)
        self.item_count += 1

    def deQueue(self):
        if not self.is_Empty():
            self.delete_first()
            self.item_count -= 1

    def get_front(self):
        if not self.is_Empty():
            return self.start.item

    def get_last(self):
        if not self.is_Empty():
            temp =self.start
            while temp is not None:
                if temp.next == None:
                    return temp.item
                temp = temp.next
    
    def Printing(self):
        return super().print()
    
    def size(self):
        return self.item_count
    

q1= Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
q1.enQueue(40)
q1.enQueue(50)
q1.Printing()
q1.deQueue()
print()
print(f"The Front Element Of Queue is :{q1.get_front()}")
print(f"\nThe last Element Of Queue is :{q1.get_last()}")
print(f"The Size of Queue is : {q1.size()}")









































































# from demo_sll import *
# class Stack(sll):
#     def __init__(self):
#         super().__init__()  #this is compulsory to call parent class init method if we dont it willnot make self object and we face the error
#         # this is the way to call parent class method from child class when the both class name is same in parent and child class
#         self.item_count = 0


#     def is_empty(self):
#         return super().is_empty()
    
#     def push(self,data):
#         self.insert_at_first(data)
#         self.item_count +=1
        

#     def pop(self):
#         if not self.is_empty():
#             self.delete_first()
#             self.item_count -= 1
            

#     def peek(self):
#         if not self.is_empty():
#             return self.start.item
        
#     def size(self):
#         return self.item_count
    
# s1=Stack()
# s1.push(10)        
# s1.push(20)        
# s1.push(30)        
# print(f"The top element is :{s1.peek()}")
# s1.pop()
# print(f"The top element is :{s1.peek()}")
# s1.size()
