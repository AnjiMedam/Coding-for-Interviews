#  program to interchange  first element and last element in list
 
# list = []

# while True:
    
#     ele = int(input("enter the element for list : "))
#     list.append(ele)
#     if len(list)==6:
#         break
# firs_pos =0
# last_pos =len(list)-1
# for i in range(0,len(list)):
#     if i == firs_pos:
#         list.insert(i,list[last_pos])
#     if i== last_pos:
#         list.insert(i,list[firs_pos])       
# print(list)




#  program to interchange  first element and last element in list
def swapingLsit(list):
    size = len(list)
    temp = list[0]
    list[0]=list[size-1]
    list[size-1]=temp

    return list

list = [2,3,4,6,7,8]
print(swapingLsit(list))















