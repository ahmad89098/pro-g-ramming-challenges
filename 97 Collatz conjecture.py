# Pro/g/ramming Challenges
# 97: Collatz conjecture
# by ahmad89098

# Start with any positive integer n
# If the previous term is even, the next term is one half the previous term.
# If the previous term is odd, the next term is 3 times the previous term plus 1

n = int(input("Enter any number"))
while n != 1:
    if n % 2 == 0:
        n = 0.5*n
    else:
        n = (3*n) + 1
    print(n)