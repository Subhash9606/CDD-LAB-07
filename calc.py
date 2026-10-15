# calc.py
num1 = 10
num2 = 5
op = "add"

# Do the math
if op == "add":
    result = num1 + num2
elif op == "subtract":
    result = num1 - num2
elif op == "multiply":
    result = num1 * num2
elif op == "divide":
    result = num1 / num2

print("Result:", result)