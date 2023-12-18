# Reverse Words in a Given String in Python

'''
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks
'''
str_item=input("enter the string sentence..!: ")
list_item = str_item.split(" ")
list_words=[]
for word in list_item:
    empty_str=""
    strTolist= list(word)
    strTolist.reverse()
    for s in strTolist:
        empty_str+=str(s)
    
    list_words.append(empty_str)
    empty_str=""
print(list_item)    
print(list_words)    







