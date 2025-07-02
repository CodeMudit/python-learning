tuple = (90,23,2,3,45,67) # () are used to create a tuple intead of [] 
print(type(tuple))

# We cannot change the elements in a tuple just like strings

tuple1 = () # We can create an empty tuple
tuple2 = (1,) # To create a single element tuple we need to put a comma 
tuple4 = (1) # It will be counted as an integer not tuple
tuple3 = (1,2) # Not necessary to put a coma in the end if there are multiple elements

# Tuple Methods

tup = (1,2,3,4,5,6,7)
print(tup[1:3]) # In tuple we consider elements and not index it will print the elements between 1 and 3 
print(tup.index(2)) # It will print the index of element 2 
print(tup.count(3)) # It will count the number of occurences of the element 3 

