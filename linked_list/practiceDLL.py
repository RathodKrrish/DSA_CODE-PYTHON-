class node :
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start):
        self.start=start

    def is_empty(self):
        return self.start == None
    
    def printing(self):
        temp=self.start
        while temp != None:
            print(temp.item,end=' ')
            temp=temp.next

    def searching(self,data):
        if not self.is_empty():
            temp=self.start
            while temp != None:
                if temp.item == data:
                    return temp
                temp=temp.next
            return None
    
    def insertion_at_start(self,data):
        if self.is_empty():
            n=node(data)
            self.start=n
        else:
            n=node(data,self.start)
            prev=self.start
