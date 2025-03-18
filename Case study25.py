# Grocery List Program

def grocery_list():
    print("🛒 Welcome to the Grocery List Manager! 🛒")

    groceries = []  # Empty list to store grocery items

    while True:
        item = input("Enter a grocery item (or type 'done' to finish): ").strip()

        if item.lower() == "done":
            break  # Stop adding items

        groceries.append(item)  # Add item to the list
        print(f"✅ '{item}' added to the list!")

    # Display the final grocery list
    if groceries:
        print("\n📋 Your Grocery List:")
        for i, item in enumerate(groceries, start=1):
            print(f"{i}. {item}")
    else:
        print("Your grocery list is empty!")

# Run the function
grocery_list()
