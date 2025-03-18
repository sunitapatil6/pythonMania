# Age Categorization Program

def categorize_age():
    print("👶👦🧑👴 Age Categorizer 👶👦🧑👴")

    # Get the user's age
    age = int(input("Enter your age: "))

    # Determine the category
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age <= 12:
        print("You are a Child. 🧒")
    elif age <= 19:
        print("You are a Teenager. 🧑‍🎓")
    elif age <= 59:
        print("You are an Adult. 🧑")
    else:
        print("You are a Senior Citizen. 👴")

# Run the function
categorize_age()
