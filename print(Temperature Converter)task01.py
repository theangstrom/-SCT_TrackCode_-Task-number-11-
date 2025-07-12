print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = input("Enter choice (1/2/3): ")
temp = float(input("Enter temperature: "))

if choice == '1':
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted}°F")
elif choice == '2':
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted}°C")
elif choice == '3':
    converted = temp + 273.15
    print(f"{temp}°C = {converted}K")
else:
    print("Invalid choice")

# This line makes the program wait before closing
input("Press Enter to exit...")