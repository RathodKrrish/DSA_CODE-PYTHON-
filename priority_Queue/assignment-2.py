class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next

class priorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start  or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp =temp.next
            n.next = temp.next
            temp.next = n 
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("PriorityQueue Is Empty!!!!...")
        data = self.start.item
        self.start=self.start.next
        self.item_count -= 1
        return data
    
    def size(self):
        return self.item_count
    

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