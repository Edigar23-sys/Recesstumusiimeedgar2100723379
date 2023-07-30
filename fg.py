student_health = {}

print("Welcome to the Student Mental Health Survey!")

# Ask for the student's name
name = input("Please enter your name: ")
student_health['Name'] = name

# Ask about their current mood
mood = input("How would you describe your current mood? ")
student_health['Mood'] = mood

# Ask about their stress level
stress_level = input("On a scale of 1 to 10, how stressed are you? ")
student_health['Stress Level'] = stress_level

# Ask about their sleep quality
sleep_quality = input("How would you rate the quality of your sleep? (Poor, Fair, Good) ")
student_health['Sleep Quality'] = sleep_quality

# Print the collected information
print("\nThank you for sharing your information!")
print("Here's what we gathered:")
for key, value in student_health.items():
    print(f"{key}: {value}")
    