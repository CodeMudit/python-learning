marks = [98,87.9,46.5,99,59] # This is type of structure is called a list
print(marks)
print(type(marks))
print(len(marks))

student = ["Mudit","Panipat",132103]
print(student)

# We can change the content of a list
# But we cannot vhange the content of a string

str = "Mudit"
print(str[0])
# str[0] = "y" This gives an error

print(student[2])
student[2] = "Delhi" # Changes the element at 2 in student
print(student) 

# List slicing

list = [1,2,3,4,5,6,7,8,8,9,0]
list1 = list.copy() # This function is used to make an exact copy of a list
print(list)
sublist = list[1:5] # 5th indx will not be included
print(sublist)
print(list1)

# Negative undex is also same in the lists as strings

# List Methods 
# All these methods return an updated value can't be print or stored in variables if stored returns none

list2 = [97,100,103,106,109,112,98]
list2.append(115) # Add 115 to the end of the list
list2.sort() # Arrange the elements of list1 in ascending order
list2.sort(reverse=True) # sort the elements in list1 in descending order
list2.reverse() # Reverse the elements in list1 
list2.insert(0,900) # insert the element in a list at a particular index 
list2.remove(900) # removes the element first appearance
list2.pop(2) # removes the element from the list at a particular index



