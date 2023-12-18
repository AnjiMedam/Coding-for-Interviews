#  Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

l = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

def removeDupliacte(l):
    s1=set()
    s2=set()
    for ele in l:
        if ele not in s1:
            s1.add(ele)
        else:
            s2.add(ele)
    print("after removed duplicate:", list(s1))
    print("duplicate element: ", list(s2))
    
removeDupliacte(l)            





















