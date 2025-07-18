class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class cll:
    def __init__(self,last=None):
        self.last = last
    
    def is_empty(self):
        return self.last == None
    
    
    def searching(self,data):
        if self.is_empty():
            return None
        
        temp =self.last
        while temp !=self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    


    def printing(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end =' ')
                temp = temp.next
            print(temp.item)

    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n

        else:
            n.next = self.last.next
            self.last.next = n

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n


    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n

        else:
            n.next = self.last.next
            self.last.next = n
            self.last =n
        
    def delete_at_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next =self.last.next.next

    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_at_first()
                else:
                    temp= self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_at_last()
                                break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next


    def delete_at_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp=temp.next
                temp.next = self.last.next
                self.last = temp
    
    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
        
class CLLIterator:

    def __init__(self,start):
        self.start = start
        self.current = start


    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        data =self.current.item
        self.current = self.current.next
        if self.current == self.start :
            raise StopIteration
        return data

    

mylist=cll()
mylist.insert_at_first(5)
mylist.insert_at_first(4)
mylist.insert_at_first(3)
mylist.insert_at_first(2)
mylist.insert_at_first(1)
mylist.insert_after(mylist.searching(5),6)
mylist.insert_after(mylist.searching(6),7)
mylist.insert_at_last(8)
mylist.insert_at_last(9)
mylist.insert_at_last(10)
mylist.delete_at_first()
mylist.delete_at_last()
mylist.delete_item(2)
mylist.delete_item(9)

mylist.printing()

print("\n")
print("Wiith Using Iterator!!!")

for i in mylist:
    print(i,end=' ')
print()
