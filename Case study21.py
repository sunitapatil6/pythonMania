# Function to perform calculations
def calculator():
    print("🖩 Welcome to the Basic Calculator 🖩")

    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Displaying operation choices
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Taking user choice
    choice = input("\nEnter the number of the operation you want to perform: ")

    # Performing the calculation
    if choice == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid choice. Please select a valid operation.")

# Running the calculator
calculator()
