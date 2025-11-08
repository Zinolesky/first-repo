
is_running = True

while is_running:
    num1 = int(input("Enter a number: "))
    op = input("Enter an operator (+, -, *, /): ")
    num2 = int(input("Enter another number: "))

    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid input")
        is_running = False
