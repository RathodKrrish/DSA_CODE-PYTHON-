#this code is based on extending the singly linked list i Queue data Structure :-
from demo_sll import *

class Queue(sll):
    def __init__(self):
        self.mylist = sll()
        self.item_Count = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def enQueue(self,data):
        self.mylist.insert_at_last(data)
        self.item_Count += 1

    def deQueue(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_Count -= 1


    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.item

    def get_last(self):
        if not self.is_empty():
            temp = self.mylist.start
            while temp is not None:
                if temp.next == None:
                    return temp.item
                temp = temp.next

    def size(self):
        return self.item_Count

    def printing(self):
        temp = self.mylist.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next



q1 =Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
q1.enQueue(40)
q1.enQueue(50)
q1.printing()
q1.deQueue()
q1.deQueue()
print()
q1.printing()
print()
print(f"The Front Element Of Queue is :{q1.get_front()}")
print(f"\nThe last Element Of Queue is :{q1.get_last()}")
print(f"The Size of Queue is : {q1.size()}")
