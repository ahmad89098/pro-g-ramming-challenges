# Pro/g/ramming Challenges
# 89: Convert numbers to text
# by ahmad89098

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# number is being used to store the number inputted from the user
# string is the final text that needs to be printed
# Converting 2 digit numbers was easy but that wasn't the case with 3 digit numbers (hundreds)
# 100,200,300,400....etc were easy to convert
# To convert the other 3 digit numbers, I took the number in the hundred position of the input number
# and then converted it into hundred of that number
# i.e if the user number is 137, I took the 1, made it 100 and then stored 100 in string1
# Then we subtract string1 from the input number and we are left with two digits (137-100=37)
# We use the same process as we did before to convert the other 2 ten and unit digits
# Add all of them together and we get the converted text
# Yes it becomes more harder the bigger the number(obv)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
prefixes = ["", "", "", "thir", "for", "fif", "six", "seven", "eight", "nine"]

number = input("Enter the number you want to convert: ")
if len(number) == 1 or int(number) == 10 or int(number) == 11 or int(number) == 12:
    string = units[int(number)]
elif int(number) == 20:
    string = "twenty"
elif int(number) < 20:
    string = prefixes[int(number) - 10] + "teen"
# REMEMBER: word[0] gives the first letter
elif int(number) < 30:
    string = "twenty " + units[int(number[1])]
elif len(number) == 2:
    string = prefixes[int(number[0])] + "ty " + units[int(number[1])]
elif len(number) == 3:
    if number[1] == "0" and number[2] == "0":
        string = units[int(number[0])] + " hundred"
    else:
        string1 = int(number[0] + "0" + "0")
        string2 = int(number) - string1
        if len(str(string2)) == 1 or int(string2) == 10 or int(string2) == 11 or int(string2) == 12:
            string3 = units[int(string2)]
        elif int(string2) == 20:
            string3 = "twenty"
        elif int(string2) < 20:
            string3 = prefixes[int(string2) - 10] + "teen"
        # REMEMBER: word[0] gives the first letter
        elif int(string2) < 30:
            string3 = "twenty " + units[int(str(string2)[1])]
        elif len(str(string2)) == 2:
            string3 = prefixes[int(str(string2)[0])] + "ty " + units[int(str(string2)[1])]
        string = units[int(number[0])] + " hundred and " + string3

print(string)
