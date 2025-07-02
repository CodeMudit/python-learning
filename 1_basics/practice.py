# Store the following wrd meaning in a python dictionary
# table  : "a piece of furniture" , "A list of facts and figures"
# cat : "a small animal"

word_meanings = {
    "Table" : ["A piece of furniture" , "list of facts and figures"],
    "Cat" : "A small animal"
}
print(word_meanings)

# 1 class is required to study each subject how many classes are required to study each subject
# "python",'java','C++','python,'javascript','java','python','java','C++','C'

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
subject1 = len(subjects)
print(subject1)

# A programme to take input marks of 3 subject from the user and store them in a dictionary one by one

Marks = {}
sub1 = int(input("Please enter the marks of the Physics : "))
Marks.update({
    "Physics" : sub1
})
sub2 = int(input("Please enter the marks of Chemistry : "))
Marks.update({
    "Chemistry" : sub2
})
sub3 = int(input("Please enter the marks of Maths : "))
Marks.update({
    "Maths" : sub3
})
print(Marks)

sets = {9,"9.0"}

print(sets)