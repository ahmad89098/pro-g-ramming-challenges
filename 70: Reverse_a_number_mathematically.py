#Pro/g/ramming Challenges
#70: Reverse a number mathematically
#by ahmad89098

input_number = input("Which number do you want to reverse? ")
my_list = []
output_number = ""

for character in input_number:
    my_list.append(character)
my_list.reverse()

for character in my_list:
    output_number = output_number + character
print(output_number)
