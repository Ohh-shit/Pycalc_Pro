def ss():
    # Displays the list of operations available in the calculator.
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Squre Root")
    print("7. Cube Root")
    print("8. Average")
    print("9. Exit")
l="Result = "
ss() # Calls the function to display the list of operations.

# Main loop to keep the program running until the user decides to exit.
while True :
    try:
        choice = int(input("Choose the operation 1-9 => "))
        if choice == 9:
            # Exits the calculator.
            print("Exiting the calculator. Goodbye!")
            break 
        if choice in [1,2,3,4,5,8]:
             # Prompts the user to enter two numbers for chosen operation.
             a = float(input('Enter the "First" no. => '))
             b = float(input('Enter the "Second" no. => '))
             if choice == 1:
                  print(l,a+b)
             elif choice == 2:
                  print(l,a-b)
             elif choice ==3:
                  print(l,a * b)
             elif choice == 4:
                  if b == 0:
                       print("Error! Division by zero") # Error handling for division by zero.
                  else:
                       print(l,a/b)
             elif choice == 8:
                  print (l,(a+b)/2)
             elif choice == 5:
                  print (l,a**b)
        elif choice in [6,7]:
            # Prompts the user to enter a single number for chosen operation.
             x = int(input('Enter the "Value" no. => '))
             if choice == 6:
                  if x == 0:
                       print("Squre root of 0 is always 0 ")
                  else:
                       print (l,x*x)
             elif choice == 7:
                  if x == 0:
                       print("Cube root of 0 is always 0 ")# Error handling for non-numeric input.
                  else:
                       k = x*x
                       print(l,k*x)
    except ValueError:
     print("Error: Invalid input. Please enter numeric values.")
