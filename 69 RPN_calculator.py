# Pro/g/ramming challenges
# 69: RPN Calculator
# by ahmad89098


def operation(num1, num2):
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1/num2
    return answer


i = 0
number1 = int(input())

# this was to setup an infinite loop so that the calculator runs forever until it is exited manually
while i == 0:
    number2 = int(input())
    operator = input()
    result = operation(number1, number2)
    print(result)
    number1 = result 