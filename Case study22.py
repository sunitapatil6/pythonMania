# Function to convert temperatures
def convert_temperature():
    print("🌡 Temperature Converter 🌡")

    # Ask the user for temperature value and unit
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    # Convert temperature based on the unit
    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"\n{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"\n{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("\nInvalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the temperature converter
convert_temperature()
