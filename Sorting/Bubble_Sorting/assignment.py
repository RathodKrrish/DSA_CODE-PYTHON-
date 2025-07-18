#this is for BubbleSort:
def bubble_Sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(0,len(data_list)-1):
            if data_list[i] > data_list[i+1]:
                data_list[i] , data_list[i+1]=data_list[i+1] , data_list[i]

l=[22,94,32,64,77,12,1,97,93]
# print(l,"\n")
# bubble_Sort(l)
# print(l)

#this is for Modified_BubbleSort:
def modified_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(0,len(data_list)-1):
            if data_list[i] > data_list[i+1]:
                data_list[i] , data_list[i+1] = data_list[i+1] , data_list[i]
                flag=True
        if flag is False:
            break
    
# print(l,"\n")
# modified_bubble_sort(l)
# print(l)

#this is for Selection_Sort:
def selection_sort(data_list):
    n=len(data_list)
    for i in range(n):
        min_value=i  #means it will assign 0 index value in min_value
        for j in range(i+1,n): #here we took i+1 because we already have min_value mean i so now we have to compare i with i+1 to end of list.
            if data_list[j]<data_list[min_value]:
                min_value=j
        data_list[i],data_list[min_value]=data_list[min_value],data_list[i]

# print(l,"\n")
# selection_sort(l)
# print(l)

# this is for insertion sort:
def insertion_Sort(data_list):
    for i in range(1,len(data_list)):
        temp=data_list[i]
        j=i-1
        while j>=0 and temp<data_list[j]:
            data_list[j+1] = data_list[j]
            j-=1
        data_list[j+1] =temp
# insertion_Sort(l)
# print(l)

# this is for Quick sort:
def quick_Sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot=data_list[0]  #to initilize
        lesser=[x for x in data_list[1:] if x<= data_list[0]]
        greater=[x for x in data_list[1:] if x>= data_list[0]]
        return quick_Sort(lesser)+[pivot]+quick_Sort(greater)

# mylist=[56,1,14,28,34,49,61,72,88,99]
# result=quick_Sort(mylist)
# print(mylist)
# print(result)
        
# this is for merge sort:
         
def merge_sort(list1):
    if len(list1) > 1:
        mid=len(list1) // 2
        left=list1[:mid]
        right=list1[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i+=1
            else:
                list1[k] = right[j]
                j+=1
            k+=1
        while i< len(left):
            list1[k]=left[i]
            i+=1
            k+=1

        while j< len(right):
            list1[k]=right[j]
            j+=1
            k+=1

mylist=[75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(mylist)
print(mylist)