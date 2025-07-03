# Creating a function to find the average of 3 Numbers 

def calc_avg(a,b,c) :
    average = (a+b+c)/3
    print(average)
    return average

calc_avg(10,11,12)

# Write a function to print the length of a list

def list_len(list) :
    print(len(list))
    return len(list)

avengers = ["Ironman","Thor","Hulk","Captain America"]
list_len(avengers)

# Write a function to print the elements of a list in a single line 

def single_line(list) :
    for items in list :
        print(items, end = " ")
    return list

single_line(avengers)

# Write a function to find the factorial of n (n is the parametre)

def factorial(n) :
    i = 1
    j = 1
    while j <= n :
        i *= j
        j += 1
    print(i)

factorial(5)
factorial(3)

# Write a function to convert USD to INR

def usd_conversion(a) :
    convert = a*83
    print(a ,"USD = ",convert,"INR")
    return(convert)

usd_conversion(80)

# Write a function that takes a output number from the user and prints the string odd or even

def odd_eve() :
    number = int(input("Enter a number : "))
    if (number%2 == 0) :
        print("Even")
    elif (number == 0) :
        print("0 is neither odd nor even")
    else :
        print("Odd")

        
odd_eve()

# Write a recursive function to calculate the sum of first n natural numbers 


def N_num(n) :
    if n == 0 :
        return 0
    return N_num(n-1) + n 
    

print(N_num(10))

# Write a programme to print all the elements of a list 

def list_print(list1, idx = 0) :
    if idx == len(list1) :
        return 
    print(list1[idx])
    list_print(list1,idx+1)

fruits = ["Mango","Litchi","Banana"]
list_print(fruits)
    