# Python program to print all negative numbers in a range

# Input: a = -4, b = 5
# Output: -4, -3, -2, -1

item=[-4,5]
def printingNegative(item):
    for i in item:
        if i<0:
            while i<0:
                print(i,end=" ")
                i=i+1


printingNegative(item)










