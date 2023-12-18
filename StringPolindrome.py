# Python program to check whether the string is Symmetrical or Palindrome
''''
Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome
'''
str_item=input("Enter the your string :")

list_item=list(str_item)
list_item.reverse()
# print(list_item)
after_reverse =""
for ele in list_item:
    after_reverse+=ele

print(after_reverse)
if after_reverse == str_item:
    print("Entered string is palindrome..!")
else:
    print("Entered stirng is not polindrome ..!")    


