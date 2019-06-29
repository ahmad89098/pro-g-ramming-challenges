# Pro/g/ramming Challenges
# 31: Cipher/decipher text
# by ahmad89098

# Implemented Atbash Cipher from http://rumkin.com/tools/cipher/

# A is 65 and Z is 90
# B is 66 and Y is 89


def cipher(input_text):
    output_string = ""
    for letter in input_text:
        if not letter == " " and ord(letter) >= 65 and ord(letter) <= 90:
            distance_from_a = ord(letter) - 65
            distance_from_z = 90 - distance_from_a
            output_string = output_string + chr(distance_from_z)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            distance_from_a = ord(letter) - 97
            distance_from_z = 122 - distance_from_a
            output_string = output_string + chr(distance_from_z)
        else:
            output_string = output_string + " "
    return output_string


def decipher(input_text):
    output_string = ""
    for letter in input_text:
        if not letter == " " and ord(letter) >= 65 and ord(letter) <= 90:
            distance_from_z = 90 - ord(letter)
            distance_from_a = distance_from_z + 65
            output_string = output_string + chr(distance_from_a)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            distance_from_z = 122 - ord(letter)
            distance_from_a = distance_from_z + 97
            output_string = output_string + chr(distance_from_a)
        else:
            output_string = output_string + " "
    return output_string


print("Enter 1 to cipher using Atbash")
print("Enter 2 to decipher using Atbash ")
user_choice = input()
user_text = input("Enter your text: ")
if user_choice == "1":
    print(cipher(user_text))
elif user_choice == "2":
    print(decipher(user_text))