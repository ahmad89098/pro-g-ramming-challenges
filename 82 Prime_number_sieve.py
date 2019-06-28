# Pro/g/ramming challenges
# 82: Prime number sieve
# by ahmad89098

original_list = []
prime_numbers = []

# original_list will store all the numbers up until the given limit.
# We will then separate all the prime numbers from this list (using the check_prime function)
# and save them to another list (prime_numbers)


def check_prime(number_to_check):
    prime = True
    if number_to_check == 1 or number_to_check == 0:
        prime = False
    if number_to_check != 2:
        for j in range(2, number_to_check):
            if number_to_check % j == 0:
                prime = False
    return prime

limit = int(input("Enter the number till which you want all the prime numbers: "))

for i in range(1, limit+1):
    original_list.append(i)

for number in original_list:
    if check_prime(number):
        prime_numbers.append(number)

print(prime_numbers)