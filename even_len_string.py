
# Python program to print even length words in a string
# input: My name is anji medam
# output: my name is anji

String_user = input("enter the string for print: ")

list_items =String_user.split(' ')

# empty_string =""

def print_even_words(list_items):
    
    empty_string =""
    for word in list_items:
        if len(word) % 2==0:
            empty_string += word + " "
    print("String which is containing even words only: ",empty_string)         

print_even_words(list_items)
  


















