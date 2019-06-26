# Pro/g/ramming Challenges
# 85: Fibonacci sequence (atleast the first 100 numbers)
# by ahmad89098

first_number = 0
second_number = 1

print(first_number)
print(second_number)

for i in range(1,50):
    first_number = first_number + second_number
    print(first_number)
    second_number = first_number + second_number
    print(second_number)
