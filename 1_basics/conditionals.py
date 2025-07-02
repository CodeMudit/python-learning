# If and else statement 

age  = 21 

if (age>=18) :
    print("You are eligible for a driving license")
else :
    print("you are not eligible for a driving license")

light = "Red"
if (light=="Red") :
    print("Stop")
elif (light=="Yellow") : 
    print("Wait")
elif (light=="Green") : 
    print("Go")
else :
    print("Light is broken")

marks = int(input("Please enter the marks of the student : "))
if (marks>= 90) : 
    print("The student's grade is : 'A'")
elif (marks<90 and marks>=80) : 
    print("The student's grade is : 'B'")
elif (marks<80 and marks>=70) : 
    print("The student's grade is 'C'") 
else :
    print("The student's grade is 'D'")