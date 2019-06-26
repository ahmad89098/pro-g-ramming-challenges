# Pro/g/ramming Challenges
# 57: Anagram Checker
# by ahmad89098

# the challenge said anagram checker not anagram solver.....

word = input("Enter the word you wish to check: ")
anagram = input("Enter the anagram you wish to check: ")

true = 0

if len(anagram) == len(word):
    for letter in word:
        for alphabet in anagram:
            if alphabet == letter:
                true = true + 1

if len(word) == true:
    print("Yes it is an anagram")
else:
    print("No it is not an anagram") 