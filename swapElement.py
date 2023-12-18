# Python Program to Swap Two Elements in a List
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

list = [12, 3 ,4 , 6,7]

def swapElement(list,pos1, pos2):
    size =len(list)
    temp =list[pos1-1]
    list[pos1-1]=list[pos2-1]
    list[pos2-1]=temp
    print("list after the swapped: ", list)

swapElement(list,pos1=1,pos2=3)
    








