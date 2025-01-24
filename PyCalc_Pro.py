def ss():
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
ss()
while True :
    try:
        choice = int(input("Choose the operation 1-9 => "))
        if choice == 9:
            print("Exiting the calculator. Goodbye!")
            break 
        if choice in [1,2,3,4,5,8]:
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
                       print("Error! Division by zero")
                  else:
                       print(l,a/b)
             elif choice == 8:
                  print (l,(a+b)/2)
             elif choice == 5:
                  print (l,a**b)
        elif choice in [6,7]:
             x = int(input('Enter the "Value" no. => '))
             if choice == 6:
                  if x == 0:
                       print("Squre root of 0 is always 0 ")
                  else:
                       print (l,x*x)
             elif choice == 7:
                  if x == 0:
                       print("Cube root of 0 is always 0 ")
                  else:
                       k = x*x
                       print(l,k*x)
    except ValueError:
     print("Error: Invalid input. Please enter numeric values.")