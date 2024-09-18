
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b



# Calcualator function
def calculator():
    while True:
        # Display the operation menu
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exit")
        
        # User input for choice
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        # Check for exit
        if choice == '6':
            print("Exiting the calculator.")
            break
        
        # Input validation for choice
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please choose a valid option.")
            continue
        
        try:
            # User input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = modulus(num1, num2)
            print(f"{num1} % {num2} = {result}")
        
        print()  

if __name__ == "__main__":
    calculator()
