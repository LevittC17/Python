# Enter calculation: 5 * 6
# 5 * 6 = 30

# Store the user input of 2 numbers and the operator

num1, operator, num2 = input("Enter calculation ").split()

# Convert numbers to integers

num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
if operator == "+":
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))
elif operator == "*":
    product = num1 * num2
    print("{} * {} = {}".format(num1, num2, product))
elif operator == "/":
    quotient = num1 / num2
    print("{} / {} = {}".format(num1, num2, quotient))
elif operator == "%":
    remainder = num1 % num2
    print("{} % {} = {}".format(num1, num2, remainder))
else:
    print("Check the operator again")

# print results