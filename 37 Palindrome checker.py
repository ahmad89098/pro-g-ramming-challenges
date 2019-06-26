# Pro/g/ramming Challenges
# 37: Palindrome Checker
# by ahmad89098

# check if the string spelled forwards is the same as it is spelled backwards

list_to_be_reversed = []
reversed_string = ""

input_string = input("Enter the string you wish to check: ")
for character in input_string:
    list_to_be_reversed.append(character)
list_to_be_reversed.reverse()
for value in list_to_be_reversed:
    reversed_string = reversed_string + value

if input_string == reversed_string:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")