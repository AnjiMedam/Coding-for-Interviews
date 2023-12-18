# Find Maximum of two numbers in Python
# Input: a = 2, b = 4
# Output: 4

list = [2,4,9,8]

def max_element(list):
    for i in range(0,len(list)-1):
        max_ele = list[i]
        if max_ele < list[i+1]:
            max_ele = list[i+1]
    print(max_ele)
max_element(list)        























