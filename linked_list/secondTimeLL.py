class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    #this function returns the true if the single ll is empty
    def is_empty(self):
        return self.start == None
    #this printing function iterate in sll and print the values of every node.
    def printing(self):
        temp=self.start
        while temp:
            print(temp.item,end=' ')
            temp=temp.next
    #this searchinf function is exmaple of linear searching in the sll it will help to find any soecific node or can be
    # used into the prosess of imsert after any perticular node
    def searching(self,data):
        temp=self.start
        while temp != None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    
    #from here the insertion functions are started.
    def insert_first(self,data):   
        n=Node(data,self.start)
        self.start=n
        
    def insert_after(self,temp,data):
        if temp != None:
            n=Node(data,temp.next)
            temp.next=n

    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            if self.start.next ==None:
                self.start.next=n
            else:
                temp=self.start
                while temp.next != None:
                    temp=temp.next
                temp.next=n
    # from here the deletion node is sarted..
    def delete_first(self):
        if self.is_empty():
            raise ValueError("The linked list is Underflow")
        else:
            self.start=self.start.next

    def delete_node(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp=self.start
            if temp.item == data:
                self.start==temp.next
            else:
                while temp.next != None:
                    if temp.next.item == data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def delete_last(self):
        if not self.is_empty():
            temp=self.start
            if self.start.next == None:
                self.start=None
            else:
                while temp.next.next != None:
                    temp=temp.next
                temp.next=None
    
    def reverse_list(self):
        prev = None
        current=self.start
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.start=prev
    def __iter__(self):
        return SLLiterator(self.start)

class SLLiterator:
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
    
mylist=SLL()
mylist.insert_first(20)
mylist.insert_first(10)
mylist.insert_first(0)
mylist.insert_after(mylist.searching(20),30)
mylist.insert_last(40)
mylist.insert_last(50)
mylist.insert_last(60)
mylist.printing()
mylist.delete_first()
mylist.delete_node(20)
mylist.delete_last()
print()
mylist.printing()
print()
mylist.reverse_list()
mylist.printing()
print("\nAfter Iteration the List!")
for i in mylist:
    print(i,end=" ")