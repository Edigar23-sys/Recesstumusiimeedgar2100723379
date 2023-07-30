#Control flow
#Day2 Module 2
age = 17
if age < 18:
    print("Your are under age")
if age >= 18:
    print("Your are adult")
else: 
    print("You are a senior citizen")

#Loops 
#for, while 
cars = ["Tesla", "jeep", "Ford", "Toyota", "BMW"]
for car in cars:
    print(car)
 
fruits = ["Mango", "Jack Fruit", "Avocado"]
for fruit in fruits:
    print(fruit)

#while loop
#while condition is True: I will execute while condition is true
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 5:
        print(i)

y = 0
while y < 10:
    print(y)
    y += 1

fruits02 = ["apple", "banana", "mango","Grapes"]
fruits02_count = 0
while fruits02_count < len(fruits02):
    print(fruits02[fruits02_count])
    fruits02_count += 1
#my
people = ["John", "Edgar", "David", "Emmma", "jill"]
people_count = 0
while people_count < len(people):
    print(people[people_count])
    people_count += 1
#break and Continue statements
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 6:
        break
    print(number)


emotions = {
    'happy': "I'm "
}
    

