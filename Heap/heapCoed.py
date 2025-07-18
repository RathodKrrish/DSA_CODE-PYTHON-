class Heap:
    def __init__(self):
        self.heap=[]

    def createHeap(self,list1):
        for ele in list1:#ele=elements
            self.Insert(ele)

    def Insert(self,ele):
        index=len(self.heap)
        parentIndex=(index-1)//2

        while index > 0 and self.heap[parentIndex] < ele:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index - 1)//2
        if index ==len(self.heap):
            self.heap.append(ele)
        else:
            self.heap[index]=ele
        
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()

        index= 0
        leftChildIndex=2*index+1
        rightChildIndex=2*index+2

        while leftChildIndex < len(self.heap):
            if rightChildIndex < len(self.heap):
                if self.heap[leftChildIndex]>self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex]>temp:
                        self.heap[index]=self.heap[leftChildIndex]
                        index=leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > temp:
                        self.heap[index]=self.heap[rightChildIndex]
                        index=rightChildIndex
                    else:
                        break
            else:# if no right child
                if self.heap[leftChildIndex]>temp:
                    self.heap[index]=self.heap[leftChildIndex]
                    index=leftChildIndex
                else:
                    break

            leftChildIndex=2*index+1
            rightChildIndex=2*index+2
        self.heap[index]=temp
        return max_value
    
    def heapSort(self,list1):
        self.createHeap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2



class EmptyHeapException(Exception):
    def __init__(self,msg="Heap is empty"):
        self.msg=msg

    def __str__(self):
        return self.msg
    
list1=[34,12,45,67,19,7,98,78,66,91]
h=Heap()
list2=h.heapSort(list1)
print("Heap sort : ")
print(list2)