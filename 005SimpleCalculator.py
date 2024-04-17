while True:
    try:
        # Setting up the user input
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        operation = input("Enter your arithmetic operator (+, -, *, /): ")

        # Setting up the arithmetic performance based on user input
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = num1 / num2
        else:
            print('Invalid operation, please use +, -, * or /')
            continue  # Ask for new input by continuing the loop if the operation is invalid

        # Display result
        print("Result:", result)
    
    except ValueError:
        print("Letters not allowed, please use a number")
        continue  # Ask for new input by continuing the loop if a ValueError occurs
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        continue  # Ask for new input by continuing the loop if a ZeroDivisionError occurs

    # Prompt user for the choice to perform another calculation or exit
    while True:
        choice = input("Do you want to perform another calculation? (y/n):").lower()
        if choice == 'n':
            break  # Exit the program
        elif choice == 'y':
            print("Okay!")
            break  # Continue to the next calculation
        else:
            print("Invalid choice. Please choose 'y' or 'n'")
    if choice == 'n':
        print("Calculator is shutting down, goodbye!")
        break
