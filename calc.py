def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

while True:
    try:
        operation = input("---------------\nEnter operation Number :\n1.Add \n2.Sub\n3.Mul\n4.Div\n0.Exit\n-- ")

       
        if operation == '0':
            print("Exiting the calculator. bye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please enter a valid operation (1, 2, 3, 4, 0).")

    
    except Exception as e:
        print(f"An error occurred: {e}")

