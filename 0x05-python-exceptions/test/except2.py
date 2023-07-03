user_input = input("Enter a number: ")
try:
    number = int(user_input)
    result = number / 2
    print("The result is:", result)
except ValueError:
    print("invalid input. Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
