def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y

def square(x):
    return x ** 2


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
    operation = int(input("Enter the choice (1-6): "))

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