# Program to perform simple calculation

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x , y):
    if y == 0:
        return "Division by Zero Error"
    else:
        return x / y

# Exponentiation
def square(x):
    return x ** 2

# Main Function
def main():
    print("Simple Calculator")
    
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: square
    }

    print("1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Square")
    operation = int(input("Enter the choice (1-5): "))

    if operation in operations:
        if operation == 5:
            num = float(input("Enter the number: "))
            result = operations[operation](num)
        else:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            result = operations[operation](num1, num2)

        print("Result: ", result)
    
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    main()