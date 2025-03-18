# Favorite Color Fun Fact Program

def color_facts():
    print("🎨 Welcome to the Color Fun Fact Generator! 🎨")

    # Dictionary of colors and their fun facts
    color_facts_dict = {
        "red": "Red is the color of energy, passion, and action! ❤️",
        "blue": "Blue is the most popular favorite color worldwide! 💙",
        "green": "Green symbolizes nature, growth, and harmony. 🌿",
        "yellow": "Yellow represents happiness, positivity, and sunshine! ☀️",
        "purple": "Purple is often associated with royalty and creativity! 👑",
        "black": "Black is a powerful color representing elegance and mystery. 🖤",
        "white": "White symbolizes purity, peace, and simplicity. ☁️",
        "orange": "Orange is the color of enthusiasm, warmth, and adventure! 🍊",
        "pink": "Pink is associated with love, kindness, and playfulness! 🎀"
    }

    # Get user's favorite color
    color = input("What is your favorite color? ").strip().lower()

    # Check if the color is in the dictionary
    if color in color_facts_dict:
        print(color_facts_dict[color])
    else:
        print("That's a great choice! Every color has its own beauty. 🌈")

# Run the function
color_facts()
