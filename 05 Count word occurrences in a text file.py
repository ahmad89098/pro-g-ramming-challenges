# Pro/g/ramming Challenges
# 47: Count words in a string(+lines, sentences)
# by ahmad89098

# Replace the string "B:\sample.txt" with the address of the file you want to search

f = open("B:\sample.txt", "r")
string = f.read()

no_of_words = 0
no_of_sentences = 0
no_of_lines = 0

for word in string.split():
    no_of_words = no_of_words + 1
for individual_characters in string:
    if individual_characters == ".":
        no_of_sentences = no_of_sentences + 1
for lines in f:
    print(lines)

print("There were " + str(no_of_words) + " words in the file.")
print("There were " + str(no_of_sentences) + " sentences in the file.")
print("There were " + str(no_of_lines) + " lines in the file.")

f.close()