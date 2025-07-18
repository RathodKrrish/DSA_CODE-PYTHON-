
#this is for BubbleSort:
def bubble_Sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(0,len(data_list)-1):
            if data_list[i] > data_list[i+1]:
                data_list[i] , data_list[i+1]=data_list[i+1] , data_list[i]


# this is for binary_searching.
def binary_serch(list2,data):
    ll=0
    ul=len(list2)-1
    mid=ll+ul//2
    while ll <= ul :
        if mid == data:
            return mid
        elif data < mid:
            ul = mid-1
        elif data > mid :
            ll=mid+1
        
    return None
l=[12,33,67,34,25,89,94,68,73,88,82]
bubble_Sort(l)
print(l,"\n")
data = int(input("Enter a value that you wanna search : "))

result=binary_serch(l,data)
if result != None:
    print(f"Element found at index {result}")
else:
    print("Seaching elemet is not in list")