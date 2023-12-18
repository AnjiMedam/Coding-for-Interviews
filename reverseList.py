
# Reversing a List in Python


'''
Using the slicing technique
Reversing list by swapping present and last numbers at a time
Using the reversed() and reverse() built-in function
Using a two-pointer approach
Using the insert() function
Using list comprehension
Reversing a list using Numpy

'''

# def Reverse(lst):
#    new_lst = lst[::-1]
#    return new_lst
 
 
# lst = [10, 11, 12, 13, 14, 15]
# print(Reverse(lst))



# Reversing a List in Python

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst) 
print("Using reversed() ", list(reversed(lst)))
#using while loop
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))






