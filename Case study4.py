import random

# List of fun fortune messages
fortunes = [
    "Today is your lucky day! 🍀",
    "An exciting opportunity is coming your way. 🚀",
    "You will meet someone who changes your perspective. 🤝",
    "A surprise gift is waiting for you! 🎁",
    "Something unexpected will make you smile today. 😊",
    "Be ready for an adventure—big or small! 🌍",
    "Your kindness will be rewarded in a surprising way. 💖",
    "A challenge ahead will make you stronger. 💪",
    "Someone will bring you good news soon! 📢",
    "Happiness is just around the corner. Stay positive! 🌞"
]

# Welcome message
print("🔮 Welcome to the Digital Fortune Teller! 🔮")

# Get user input
name = input("What's your name? ")
fav_number = int(input(f"Nice to meet you, {name}! What's your favorite number? "))

# Use the number to generate a fortune
fortune = random.choice(fortunes)  # Randomly select a fortune

# Display the personalized fortune message
print(f"\n{name}, based on your favorite number ({fav_number}), here is your fortune:")
print(f"✨ {fortune} ✨\n")

print("Hope you have a magical day! 🔮😊")
