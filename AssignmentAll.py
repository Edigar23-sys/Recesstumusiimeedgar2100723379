#Name : Tumusiime Edgar 
#StudentNo: 2100723379
#regNo: 21/U/23379/PS
#Recess Assignment

#Exercise 1: use values () method to return a list of all values in dictionary

person = {
    "name": "Tumusiime Edgar",
    "age": 20,
    "city": "kampala"
}


values_list = list(person.values())


print("List of values:", values_list)
keys_list = list(person.keys())
print("Keys:", keys_list)

#Exercise 2: To check if a key does exist in your dictionary


student = {
    "name": "Tumusiime Edgar",
    "age": 23,
    "University": "Makerere University"
}

# a function to check if a key exists in the dictionary
def check_key(dictionary, key):
    if key in dictionary:
        print("The key", key, "exists in the dictionary.")
    else:
        print("The key", key, "does not exist in the dictionary.")

# this checks if a key exists
key_to_check = input("Enter the key to check: ")
check_key(student, key_to_check)

#Exercise 3: How to change dictionary items, How to update

person02 = {
    "name": "Tumusiime",
    "age": 30,
    "city": "Kampala"
}

person02["age"] = 35
person02["city"] = "San Francisco"


print("Updated Dictionary:", person02)

new_info = {
    "age": 40,
    "city": "Los Angeles",
    "occupation": "Engineer"
}

person02.update(new_info)
print("Updated Dictionary after update():", person02)

#Exercise 4: How to add dictionary items, How remove Dictionary items
# Creating an empty dictionary
person03 = {}

# Adding dictionary items
person03["name"] = "Edgar"
person03["age"] = 30
person03["city"] = "Kampala"

# Printing the dictionary after adding items
print("Dictionary after adding items:", person03)

# Removing dictionary items
del person03["age"]
person03.pop("city")

# Printing the dictionary after removing items
print("Dictionary after removing items:", person03)

#Exercise 5: How you can loop through a dictionary and how to nest dictionary
# Creating a dictionary
person04 = {
    "name": "Tumusiime",
    "age": 30,
    "city": "Masaka"
}


for key in person04:
    print(key, "->", person04[key])
# Creating a dictionary
person05 = {
    "name": "Emma",
    "age": 30,
    "city": "Mbarara"
}


for key, value in person05.items():
    print(key, "->", value)

students = {
    "name": "John",
    "age": 20,
    "subjects": {
        "math": 90,
        "science": 85,
        "history": 95
    }
}


print("Math Score:", students["subjects"]["math"])
print("Science Score:", students["subjects"]["science"])
print("History Score:", students["subjects"]["history"])

#Stringss
#Exercise 1 use the len() function to determine the length of the string

Name = input("Enter your name: ")
print("Your name is", len(Name), "characters long.")

#Exercise 2 give an example of using a for loop in string 

Name02 = input("Enter your name: ")

for letter in Name02:
    print(letter)

#Exercise 3 give an example of slicing in strings

Name03 = input("Enter your name: ")

print(Name03[0:2])
print(Name03[2:5])
print(Name03[5:])

#Boleans 
#Exercise 
# Set boolean variables
is_raining = True
has_umbrella = False


if is_raining and not has_umbrella:
    print("It's raining and you don't have an umbrella. Stay indoors!")
else:
    print("You are either not raining or you have an umbrella. You can go outside.")
