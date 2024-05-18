# This function adds two numbers
def add(x, y):
    return x + y

print("Select operation:")
print("1. Add")


while True:
    # Take input from the user
    choice = input("Enter choice (1): ")

    # Check if choice is one of the four options
    if choice in ('1'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        # Check if the user wants another calculation
        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input")
