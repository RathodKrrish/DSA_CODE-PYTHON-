class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Sll:
    def __init__(self,start=None):
        self.start=start

    def is_Empty(self):
        return self.start == None
    
 
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp= temp.next
        return None
    

    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n


    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    
        
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_Empty():
            temp =self.start
            while temp.next != None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n


    def printing(self):
        temp=self.start
        while temp != None:
            print(temp.item,end=" ")
            temp=temp.next
        return temp
    

# Now The Concept Of Bubble Sorting Has BeeN Apears...
    def Bubble_sort(self):
        if not self.start or not self.start.next:
            return
        swapped=True
        while swapped :
            swapped =False
            current=self.start
            while current.next != None:
                if current.item > current.next.item:
                    current.item,current.next.item=current.next.item,current.item
                    swapped=True
                current=current.next

                
            
        


s1=Sll()
s1.insert_at_start(10)
s1.insert_at_start(20)
s1.search(20)
s1.insert_at_last(50)
s1.insert_at_last(40)
s1.insert_at_last(35)
s1.insert_at_last(5)
s1.insert_at_last(3)
s1.insert_at_last(58)
s1.printing()
s1.Bubble_sort()
print()
print("Sorted values :")
s1.printing()
