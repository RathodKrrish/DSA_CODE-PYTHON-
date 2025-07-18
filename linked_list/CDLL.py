#THIS FOLLOWING CODE IS FOR THE CIRCULAR DOUBLY LINKED LIST :-

class node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class cdll:

    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def searching(self, data):
        if not self.is_empty():
            temp = self.start
            while True:
                if temp.item == data:
                    return temp
                temp = temp.next
                if temp == self.start:
                    break
            return None
        

    def printing(self):
        if not self.is_empty():
            temp = self.start
            while True:
                print(temp.item,end=' ')
                temp = temp.next
                if temp == self.start:
                    break

    def insert_at_first(self,data):
        n=node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next =self.start
            n.prev =self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start =n

    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data)
            n.next = temp.next
            temp.next.prev = n
            temp.next = n
            

    def insert_at_last(self,data):
        n=node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.prev =self.start.prev
            n.next =self.start
            self.start.prev.next = n
            self.start.prev =n
       


    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev = self.start.prev
                self.start=self.start.next

    def delete_item(self,data):
        if not self.is_empty():
            temp = self.start
            start =self.start
            if temp.item==data :
                self.delete_first()
            else:
                temp =temp.next
                while temp != start:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        temp.next.prev =temp.prev
                    temp = temp.next
            
    



    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next =self.start
                self.start.prev=self.start.prev.prev

    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:

    def __init__(self,start):
        self.current =start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data
    
mylist = cdll()
mylist.insert_at_first(5)
mylist.insert_at_first(3)
mylist.insert_at_last(6)
mylist.insert_at_last(7)
mylist.insert_after(mylist.searching(3), 4)  # List: 3, 4, 5, 6, 7
print("List before deletion:")
mylist.printing()  # Expected: 3 4 5 6 7

print("\nDeleting 4:")
# mylist.delete_item(4)  # Deleting the node with value 4

print("List after deletion:")
mylist.printing()  # Expected: 3 5 6 7


for i in mylist:
    print(i,end=' ')
