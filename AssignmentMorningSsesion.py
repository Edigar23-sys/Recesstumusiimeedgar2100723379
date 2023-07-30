#Name : Tumusiime Edgar 
#StudentNo: 2100723379
#regNo: 21/U/23379/PS
#Recess Assignment

 #write a program to ask a student about their mental health.   
student_health = {}

print("Welcome to the Student Mental Health Survey!")


name = input("Please enter your name: ")
student_health['Name'] = name


mood = input("How would you describe your current mood? ")
student_health['Mood'] = mood

stress_level = int(input("On a scale of 1 to 10, how stressed are you? "))
student_health['Stress Level'] = stress_level


sleep_quality = input("How would you rate the quality of your sleep? (Poor, Fair, Good) ")
student_health['Sleep Quality'] = sleep_quality


print("\nThank you for sharing your information!")
print("Here's what we gathered:")
for key, value in student_health.items():
    print(f"{key}: {value}")


if stress_level > 6:
    print("\nIt seems that you are in a bad mental health condition. Please consider seeking support.")




    