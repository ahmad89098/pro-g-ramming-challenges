# Pro/g/ramming Challenges
# 86: Temperature converter
# by ahmad89098


def celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = (int(temp_celsius)*1.8)+32
    print(temp_fahrenheit)


def fahrenheit_to_celsius(temp_fahrenheit):
    temp_celsius = (int(temp_fahrenheit)-32) * (5/9)
    print(temp_celsius)


def celsius_to_kelvin(temp_celsius):
    temp_kelvin = int(temp_celsius) + 273
    print(temp_kelvin)


def kelvin_to_celsius(temp_kelvin):
    temp_celsius = int(temp_kelvin) - 273
    print(temp_celsius)


def fahrenheit_to_kelvin(temp_fahrenheit):
    temp_kelvin = ((int(temp_fahrenheit)-32) * (5/9)) + 273
    print(temp_kelvin)


def kelvin_to_fahrenheit(temp_kelvin):
    temp_fahrenheit = int(temp_kelvin) - 273
    temp_fahrenheit = (int(temp_fahrenheit)*1.8)+32
    print(temp_fahrenheit)


print("////////////////////////////////////")
print("TEMPERATURE CONVERTER")
print("Press 1 for fahrenheit to celsius")
print("Press 2 for celsius to fahrenheit")
print("Press 3 for celsius to kelvin")
print("Press 4 for kelvin to celsius")
print("Press 5 for fahrenheit to kelvin")
print("Press 6 for kelvin to fahrenheit")
print("////////////////////////////////////")

user_choice = input()
temp = int(input("Enter the temperature"))

if user_choice == "1":
    fahrenheit_to_celsius(temp)
elif user_choice == "2":
    celsius_to_fahrenheit(temp)
elif user_choice == "3":
    celsius_to_kelvin(temp)
elif user_choice == "4":
    kelvin_to_celsius(temp)
elif user_choice == "5":
    fahrenheit_to_kelvin(temp)
elif user_choice == "6":
    kelvin_to_fahrenheit(temp)
