# Welcome message
print("Welcome to the Personalized Story Generator!")

# Get user inputs
name = input("Enter a name: ")
object = input("Enter an object: ")
place = input("Enter a place: ")

# Pre-written story template
story = f"""
Once upon a time, {name} found a mysterious {object} while exploring {place}. 
Little did they know, this {object} held magical powers that could change their life forever!
What happened next? Only time will tell...
"""

# Display the final story
print("\nHere is your story:\n")
print(story)
print("Hope you enjoyed your mini adventure! 😊")
