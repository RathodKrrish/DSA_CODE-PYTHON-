class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class dll:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self,data):
        temp= self.start
        if not self.is_empty():
            while temp.next != None:
                temp = temp.next
        n=node(temp,data,None)
        if temp == None:
            self.start = n
        else:
            temp.next =n
    
    def insert_after(self,temp,data):
        if temp != None:
            n=node(temp,data,temp.next)
            if temp.next != None:
                temp.next.prev= n
            temp.next = n



    def searching(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None


    def printing(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            self.start =self.start.next
            self.start.next.prev =None
    
    def delete_last(self):
        if self.start is None:
            print("The Follwing list is Empty")

        elif self.start.next == None:
            self.start = None

        elif not self.is_empty():
            temp = self.start
            while temp.next.next != None:
                temp= temp.next
            temp.next = None
        else:
            pass

    def delete_Node(self,data):
        if self.start == None:
            print("linked list is EMPTY...")
        else:
            temp =self.start
            while temp != None:
                if temp.item == data:
                    if temp.next != None:
                        temp.next.prev = temp.prev
                    if temp.prev != None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

#iterator:-
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:

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
        
