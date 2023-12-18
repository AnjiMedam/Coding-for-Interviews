# Python | Word location in String
import re 

String = input("enter the string " )

 
word = input("enter the word for lacate: ")
def word_location(String, word):
    res = -1 
    list_item = String.split()
    for idx in list_item:
         if len(re.findall(word,idx))>0:
              res = list_item.index(idx)+1

    print("after the result :",res)          

word_location(String,word)





























