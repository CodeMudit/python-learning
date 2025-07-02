# Sets
# Sets store unique elements within it
# No order is followed in sets 

nums = {1,2,3,4,5,6}
set2 = {1,2,3,3,3,3,3,3,4} # Duplicate values will not be printed
print(nums)
print(set2)
print(type(nums))
print(type(set2))

print(len(nums))
print(len(set2)) # Duplicate values will not be counted
# No changes can be made in sets 
# We cannot store list or dictionaries in sets

# Creating an empty set 

null_set = set()
print(null_set)

# Methods in sets 

set = {1,2,3,4,5,6,7,8,9,0}
set1 = (12,13,14,15,16,1,2,3,4,5,5)
print(set.add(11)) # Adds the element 11 to the set
print(set.remove(11)) # Removes the given element from the set
print(set.clear()) # Makes the set empty
print(set.pop()) #prints Removes a random value from the set
print(set.union(set1)) # Combines all the unique values present inside 2 sets
print(set.intersection(set1)) # Print all the common values of 2 sets
# A set can be manipulated but the elements inside a set cannot


