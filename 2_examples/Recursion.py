# Recursions 
# It is ehn a function calls itself repeatedly

# Recursive function
def show(n) :
    if n == 0 : # --> Base case 
        return
    print(n)
    show(n-1)
    print("END")
       
# Factorial through recursion

def fact(n) :
    if (n==0 or n==1) :
        return 1 
    else :
        return n * fact(n-1)

print(fact(5))

