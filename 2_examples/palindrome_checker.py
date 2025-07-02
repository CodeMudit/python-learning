# A programme to check if a list contains a palindrome of elements

list = ["Mudit",132103,1132103,"Mudit"]
copied_list = list.copy()
copied_list.reverse()
if copied_list==list :
    print("The list contains a palindrome of elements")
else :
    print("The list do not contain a palindrome of elements")
