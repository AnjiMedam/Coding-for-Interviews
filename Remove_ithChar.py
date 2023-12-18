# How to Remove Letters From a String in Python
'''
Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
'''
'''
Using str.replace()
Using translate()
Using recursion
Using Native Method
Using slice + concatenation
Using str.join()
Using bytearray
Using removeprefix()
'''

import regex as re
test_str = "anji654medam"
new_str = ""
num =re.findall([0-9],test_str)
for i in range(len(test_str)):

    if i!=num:

        new_str = new_str + test_str[i]
print ("The string after removal of i'th character : " + new_str)










