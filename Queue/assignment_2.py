# this Code is based on inheriting list in Queue data structure:...

class Queue(list):

    count_item = 0
    def is_empty(self):
        return self == 0

    def enQueue(self,data):
        self.append(data)
        self.count_item += 1

    def deQueue(self):
        if not self.is_empty():
            self.pop(0)
            self.count_item -= 1
        else:
            raise IndexError("Queueis underFlow!")
        
    def get_Front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queueis underFlow!")
        
    def get_Last(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queueis underFlow!")
        
    def Size(self):
        return self.count_item
    
Q1= Queue()
Q1.enQueue(10)
Q1.enQueue(20)
Q1.enQueue(30)
Q1.enQueue(40)
Q1.enQueue(50)
Q1.enQueue(70)
print(f"after enQueue list is : {Q1}")
Q1.deQueue()
Q1.deQueue()
print(f"after deQueue list is : {Q1}")
print(f"the first element of list is : {Q1.get_Front()}")
print(f"the last element of list is : {Q1.get_Last()}")
print(f"the size of list is : {Q1.Size()}")

