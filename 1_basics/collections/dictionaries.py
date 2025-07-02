# Dictionaries

# Dictionaries are used to store data in key value pairs 

dict1 = {
    "Name" : "Mudit",
    "CGPA" :  9.6,
    "City" : 132103,
    "Age" : 17,
    "Degree" : "Btech"
}
print(dict1)
dict1["Degree"] = "BCA" #overwrite the value of the key
dict1["Surname"] = "Sapra" # Add a new key value pair in the dictionary


# We can change elements in a dictionary 
# There is no index in dictionary
# We can't create duplicate keys in a dictionary

# Creating a null dictionary 

dict2 = {}
print(dict2)

# Nested dictionaries
# When we create a dictionary inside of a dictionary

student = {
    "Name" : "Mudit",
    "Marks" : {
        "Physics" : 58,
        "Chemistry" : 57,
        "Maths" : 48
    }
}
print(student["Marks"]["Chemistry"])

# Dictionary Methods



mydict = {
    "Haryana" : "Chandigarh",
    "Arunachal Pradesh" : "Itanagar",
    "Sikkim" : "Gangtok",
    "Karnataka" : "Banglore",
    "West Bengal" : "Kolkata"
}

print(mydict.keys()) # Print all the keys of mydict it doesnot include nested keys
print(list(mydict.keys())) # Creates a list of the keys 
print(len(mydict)) # Print the number of keys in the dictionary
print(mydict.values()) # Print all the values in a dictionary
print(mydict.items()) # Return all the key value pairs as a tuple 

print(mydict["Haryana"]) # Also prints the value of a given key gives error if the key given in written wrong
print(mydict.get("Haryana3")) # Prints the value of a given key dies not give any type of an error 
mydict["Name"] = "Mudit"
mydict["Age"] = 17 
print(mydict)
mydict.update({
    "City" : "Panipat",
    "Year" : 2025
}) # Adds or updates the keys and values in a dictionary 

print(mydict)

