# Functions 
# These are block of statements that perform a specific task

a = 5
b = 10
sum = a+b # So many lines are being used only to get sum of two numbers
print(sum)

# TO create a function def keyword is used

# Function to get sum of two numbers

def calc_sum(a,b) : # The values in the brackets are called parametres
    sum = a+b
    print(sum)
    return (sum)

calc_sum(100,90) # The elements in the brackets are called arguments 


#Funtion definition
def difference(c,d) : 
    return (c-d)

#FUnction call
subtract = difference(10,7)
print(subtract)

def print_hello() : # In this fuction we do not have any parametres 
    print("Hello") # and we did not return any value 
                      
print_hello()

output = print_hello
print(output) # Now this will give the output as None as we did not return any value
              # If we do not return a value of a function it cannot be stored in a variable and gives the output None 

# Defualt parametres
def calc_product(a = 3,b = 2) : # the last parameter cannot be left empty if the first has a default value 
    print(a*b)
    return a*b
calc_product()
   
