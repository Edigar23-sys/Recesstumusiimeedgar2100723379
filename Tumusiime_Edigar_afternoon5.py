#Tumusiime edigar
#2100723379
#21/U/23379/PS


import traceback

print("#" * 80)
print("Exception Handling With Try & Except")
number = input("Enter a number: ")
try:
    number = int(number)
    print(number)
except ValueError as err:
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

print("#" * 80)
print("Exception Handling using raise")
number = input("Enter a number: ")
try:
    number = int(number)
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    print(number)
except ValueError as err:
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

print("#" * 80)
print("Exception Handling using assert")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
    print(number)
except AssertionError as err:
    print("Invalid input. Please enter a number")
    traceback.print_exc()
    print(f"Error: {err}")
print("#" * 80)
print("\n")

print("#" * 80)
print("Exception Handling using else")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")

print("#" * 80)
print("Exception Handling using finally")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0, "Negative numbers are not allowed"
finally:
    print(number)
    print("This code will always run")
print("#" * 80)
print("\n")

print("#" * 80)
print("Multiple except clauses")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
except ValueError:
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")

print("#" * 80)
print("Exceptions as a tuple in a single except clause")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except (AssertionError, ValueError):
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")

print("#" * 80)
print("create a file with its contents")
filename = input("Enter a filename: ")
extension = input("Enter the extension of the file: (e.g txt, py, html etc) ")
contents = input("Enter the contents of the file: ")

f = open(f"{filename}.{extension}", "w")
f.write(contents)
f.close()
print("#" * 80)
print("\n")

print("#" * 80)
print("To open a file for reading it is enough to specify the name of the file:")
print(f"Opening the file {filename}.{extension}...")
f = open(f"{filename}.{extension}")
print("Reading its contents...")
print(f.read())
print("#" * 80)
print("\n")

print("#" * 80)
print("Read Only Parts of the File")
f = open(f"{filename}.{extension}", "r")
print("Reading the first 5 characters...")
print(f.read(5))
print("#" * 80.)
