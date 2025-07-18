# this code is based on the Single Linked List of Queue Data Structure:


class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.start = None
        self.count_Item = 0

    def is_Empty(self):
        return self.start == None
    
    def size(self):
        return self.count_Item

    def Printing(self):
        temp = self.start
        while temp is not None:
            print(temp.item ,end=' ')   
            temp = temp.next

    def enQueue(self,data):
        n=Node(data)
        if self.is_Empty():
            self.start = n
            self.count_Item += 1
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            self.count_Item += 1
    def deQueue(self):
        if self.start is not None:
            self.start = self.start.next
            self.count_Item -=1

    def get_front(self):
        if self.start is not None:
            return self.start.item

    def get_last(self):
        if not self.is_Empty():
            temp = self.start
            while temp is not None:
                if temp.next == None:
                    return temp.item
                temp=temp.next
        else:
            raise IndexError("queue is empty!")



                

q1 =Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
q1.enQueue(40)
q1.enQueue(50)

q1.Printing()

print(f"\nThe Size of inked list is :{q1.size()}")
q1.deQueue()
q1.deQueue()
q1.Printing()
print(f"\nThe Size of inked list is :{q1.size()}")
print(f"\nThe Front Node of inked list is :{q1.get_front()}")
print(f"\nThe last Node of inked list is :{q1.get_last()}")

































# class node:
#     def __init__(self,item=None,next=None):
#         self.item = item
#         self.next = next

# class sll:
#     def __init__(self,start=None):
#         self.start =start

#     def is_empty(self):
#         return self.start == None
    
#     def search(self,data):
#         temp = self.start
#         while temp is not None:
#             if temp.item == data:
#                 return temp
#             temp= temp.next
#         return None
    
#     def insert_at_first(self,data):
#         n=node(data,self.start)
#         self.start = n

#     def insert_at_last(self,data):
#         n = node(data)
#         if not self.is_empty():
#             temp = self.start
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next= n
#         else:
#             self.start = n
#     def insert_after(self,temp,data):
#         if temp is not None:
#             n=node(data,temp.next)
#             temp.next = n
#     def print(self):
#         temp = self.start
#         while temp is not None:
#             print(temp.item,end=' ')
#             temp = temp.next

#     def delete_first(self):
#         if self.start is not None:
#             self.start = self.start.next
    
#     def delete_last(self):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             self.next =None
#         else:
#             temp =self.start
#             while temp.next.next is not None:
#                 temp = temp.next
#             temp.next = None


#     def delete_item(self,data):
#         if self.start is None:
#             pass

#         elif self.start.next is None:
#             if self.start.item == data:
#                 self.start =None
#         else:
#             temp = self.start
#             if temp.item == data:
#                 self.start = temp .next
#             else:
#                 while temp.next is not None:
#                     if temp.next.item == data:
#                         temp.next =temp.next.next
#                         break
#                 temp = temp.next
   

#     def __iter__(self):
#         return SLLIterator(self.start)
    
# class SLLIterator:

#     def __init__(self,start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data = self.current.item
#         self.current = self.current.next
#         return data

# mylist= sll()
# mylist.insert_at_first(20)
# mylist.insert_at_first(10)
# mylist.insert_at_last(30)
# mylist.insert_at_last(40)
# mylist.insert_at_last(70)

# mylist.insert_after(mylist.search(40),50)
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(30)

# mylist.print()
# mylist.is_Empty()
# print()

# print("After Iteration the List!")
# for i in mylist:
    # print(i,end=" ")

# class Node:
#     def __init__(self,item=None,next=None):
#         self.item =item
#         self.next = next
# class Stack:
#     def __init__(self):
#         self.start = None
#         self.item_count = 0

#     def is_empty(self):
#         return self.start == None

#     def push(self,data):
#         n=Node(data,self.start)
#         self.start = n 
#         self.item_count += 1

#     def pop(self):
#         if not self.is_empty():
#             data = self.start.item
#             self.start = self.start.next
#             self.item_count -= 1
#             return data
#         else:
#             raise IndexError("Stack Is Empty!")
        
#     def peek(self):
#         if not self.is_empty():
#             return self.start.item
#         else:
#             raise IndexError("Stack Is Empty!")
        
#     def size(self):
#         return self.item_count
    
# s1=Stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print(f"total element in stack is {s1.size()}")
# print(f"top element in stack is {s1.peek()}")
# print(f"the poping element is {s1.pop()}")
# print(f"total element in stack is {s1.size()}")
# print(f"top element in stack is {s1.peek()}")