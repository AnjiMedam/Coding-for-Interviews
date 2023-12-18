# Find length of a string in python (6 ways)

string_item=input("enter the string you wnat : ")

def findLength(string_item):
    print("By usign built in python method==>",len(string_item))

    Sum_string =  sum(1 for i in string_item)
    print(" by using sum method => ",Sum_string)


findLength(string_item)




















