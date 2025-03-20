# Function to perform the chosen operation
def calculator():
    # Get user input for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the chosen operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operation! Please choose +, -, *, or /."

    # Print the result
    return f"The result of {num1} {operation} {num2} is: {result}"

# Call the function
print(calculator())
