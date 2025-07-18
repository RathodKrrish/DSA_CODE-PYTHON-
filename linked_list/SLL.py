class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class sll:
    def __init__(self,start=None):
        self.start =start

    def is_empty(self):
        return self.start == None
    
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp= temp.next
        return None
    
    def insert_at_first(self,data):
        n=node(data,self.start)
        self.start = n

    def insert_at_last(self,data):
        n = node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next= n
        else:
            self.start = n
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next = n
    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.next =None
        else:
            temp =self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None


    def delete_item(self,data):
        if self.start is None:
            pass

        elif self.start.next is None:
            if self.start.item == data:
                self.start =None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next =temp.next.next
                        break
                    temp = temp.next
   

    def reverse_list(self):
        prev =None
        current = self.start
        while current:
            next_node= current.next
            current.next = prev
            prev = current
            current = next_node
        self.start = prev

    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:

    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

mylist= sll()
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_at_last(70)

mylist.insert_after(mylist.search(40),50)
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(30)

mylist.print()

print()

print("After Iteration the List!")
for i in mylist:
    print(i,end=" ")

mylist.reverse_list()
print()
for i in mylist:
    print(i,end=" ")




#second time
# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next

# class SLL:
#     def __init__(self,start=None):
#         self.start=start
#         self.nodecount=0
#     def is_Empty(self):
#         return  self.start == None
    
#     def Searching(self,data):
#         temp=self.start
#         while temp != None:
#             if temp.item==data:
#                 return temp
#             temp=temp.next
#         return None
    
#     def Printing(self):
#         temp=self.start
#         while temp != None:
#             print(temp.item,end=' ')
#             temp=temp.next

#     def Insert_at_start(self,data):
#         n=Node(data,self.start)
#         self.start=n
#         self.nodecount += 1
#     def Insert_at_after(self,temp,data):
#         if temp != None:
#             n=Node(data,temp.next)
#             temp.next=n
#             self.nodecount += 1
#     def Insert_at_last(self,data):
#         if self.is_Empty():
#             n=Node(data)
#             self.start=n
#             self.nodecount += 1
#         else:
#             n=Node(data)
#             temp=self.start
#             while temp.next != None:
#                 temp=temp.next
#             temp.next=n
#             self.nodecount += 1

#     def delete_at_first(self):
#         if self.start != None:
#             self.start=self.start.next
#             self.nodecount -= 1
#     def delete_after(self,temp):
#         if self.is_Empty():
#             print("Single Linked list is already Empty!")
#         else:
#             if temp != None:
#                 temp.next=temp.next.next
#                 self.nodecount -= 1
#             else:
#                 print("Searched Element are Not Founded In Single Linked List..")

#     def delete_item(self,data):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             if self.start.item==data:
#                 self.start=None
#                 self.nodecount -= 1
#         else:
#             temp=self.start
#             if temp.item == data:
#                 self.start == temp.next
#                 self.nodecount -= 1
#             else:
#                 while temp.next != None:
#                     if temp.next.item == data:
#                         temp.next=temp.next.next
#                         self.nodecount -= 1
#                         break
#                     temp=temp.next
#     def delete_last(self):
#         if not self.is_Empty():
#             temp=self.start
#             if self.start.next is None:
#                 self.start == None
#                 self.nodecount -= 1
#             else:
#                 while temp.next.next != None:
#                     temp=temp.next
#                 temp.next=None
#                 self.nodecount -= 1
                

#     def reverse_list(self):
#         prev=None
#         current=self.start
#         while current:
#             next_node=current.next
#             current.next=prev
#             prev = current
#             current=next_node
#         self.start=prev

# singleLL=SLL()
# singleLL.Insert_at_start(10)
# singleLL.Insert_at_after(singleLL.Searching(10),20)
# singleLL.Insert_at_last(30) 
# singleLL.Insert_at_last(50) 
# singleLL.Insert_at_last(60) 
# singleLL.Insert_at_start(1) 
# singleLL.Insert_at_after(singleLL.Searching(30),40)
# singleLL.Printing()
# print()
# singleLL.delete_at_first()
# singleLL.delete_after(singleLL.Searching(30))
# singleLL.delete_item(20)
# singleLL.delete_last()
# singleLL.Printing()
# print(f"\nThe number of node in list is : {singleLL.nodecount}\n")
# singleLL.reverse_list()
# singleLL.Printing()