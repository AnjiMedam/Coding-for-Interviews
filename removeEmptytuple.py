# Remove empty tuples from a list

#Method one
def RemoveEmptyTuples(tuples):
    tuple_items = filter(lambda x: x != (), tuples)
    return tuple_items
tuple1 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('', ''), ()]
result = RemoveEmptyTuples(tuple1)
print("Using filter()", list(result))

# Method Two
def Remove2(tuples):
    for i in tuples:
        if(len(i) == 0 or i==()):
            tuples.remove(i)
    return tuples

tuple2 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print("Using if conditon: ",Remove2(tuple2)) 


