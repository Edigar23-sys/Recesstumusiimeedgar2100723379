#string , int, list, int, tuples, dictionary, sets 
#list, dictionary, sets, tuple
w = 40
print(type(w))
z = "hello world"
print(type(z))
students = {
    "am okay"
}
# lists they are used to store many things in a single variable 
#afternoon = ["Trevor", "Peter", "blessing"]
#print(type(afternoon))
#print(afternoon)
#print(afternoon[0])
#print(afternoon[1])
#print(afternoon[2])n
#for i in afternoon:
 #   print(i)#

#duplicates in lists 
afternoon = ["Trevor", "Peter", "blessing", "Trevor", "Peter", "blessing"]
print(afternoon)

# I created a dictionary for a student then did a few operations on it
student = {
    "name": "TUMUSIIME EDGAR",
    "age": 20,
    "major": "SOFTWARE ENGINEERING",
    "gpa": 3.8
}

# this is how to Access dictionary elements
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# this is to Modify dictionary elements
student["age"] = 21
student["gpa"] = 3.9

# Adding new key-value pairs
student["university"] = "ABC University"

# Removing a key-value pair
del student["major"]

# Checking if a key exists
if "major" in student:
    print("Major:", student["major"])
else:
    print("Major information not available.")

# Iterating over dictionary items
for key, value in student.items():
    print(key + ":", value)

# Checking the length of the dictionary
print("Number of items in the dictionary:", len(student))

# to clear the dictionary
student.clear()

# to check if the dictionary is empty
if not student:
    print("The dictionary is empty.")

