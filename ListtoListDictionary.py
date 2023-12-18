# Python – Convert List to List of dictionaries
'''
Input : test_list = ["Anji",22,"Ravi",23,"Raj",20,"Siva",21], key_list = ["name", "age"] 
Output : [{'name':"Anji",'id':22}, {'name':"Siva",'id':21},{'name':"Ravi",'id':23},{'name':"Raj",'id':20}] 

'''


test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
 
 
print("The original list : " + str(test_list))
 
key_list = ["name", "age"]
 

n = len(test_list)
res = []
for idx in range(0, n, 2):
    res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})
 
print("The constructed dictionary list : " + str(res))










