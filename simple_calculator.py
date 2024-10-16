def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Basic Calculator!")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == "+":
                print(f"The result is: {add(num1, num2)}")
            elif operation == "-":
                print(f"The result is: {subtract(num1, num2)}")
            elif operation == "*":
                print(f"The result is: {multiply(num1, num2)}")
            elif operation == "/":
                print(f"The result is: {divide(num1, num2)}")
            else:
                print("Invalid operation. Please choose from +, -, *, /.")

            another = input("Do you want to perform another calculation? (yes/no): ")
            if another.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculator()
