# Python program to count positive and negative numbers in a list

items= [12,-2,-4,-6,9,-3,4,6,2]
count_posi=0
count_nega=0
def Counting(items,count_posi, count_nega):
    for ele in items:
        if ele >0:
            count_posi=count_posi+1
        else:
            count_nega=count_nega+1
    print("positive elements :", count_posi)
    print("negative elements : ", count_nega)            

Counting(items,count_posi,count_nega)






