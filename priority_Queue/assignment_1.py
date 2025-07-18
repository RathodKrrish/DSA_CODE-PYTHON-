# this code is based on the list and his function for emplementing the priority Queue:

class priorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index,(data,priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("priority Queue is Empty!!...")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
    
p=priorityQueue()
p.push("Bhakti",1)
p.push("Kundal",5)
p.push("Mansi",6)
p.push("Dharmik",2)
p.push("Kuldip",4)
p.push("Prem",7)
p.push("Krrish",3)

while not p.is_empty():
    print(p.pop())