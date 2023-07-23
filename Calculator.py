import numpy as np
import os
import platform

banner = """
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                 
              Made By AmcaQt
"""

if platform.system() == "Linux":
    os.system("clear")
else:
    os.system("cls")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def power(x, y):
    return x ** y

def matrix_add(x, y):
    return np.add(x, y)

def matrix_subtract(x, y):
    return np.subtract(x, y)

def matrix_multiply(x, y):
    return np.matmul(x, y)

print(banner)
print("Select operation:")
print("1. Add                   2. Subtract")
print("3. Multiply              4. Divide")
print("5. Power")
print("")
print("Matrix Operation:")
print("1. Matrix Add")
print("2. Matrix Subtract")
print("3. Matrix Multiply")

try:
    while True:
        choice = input("Enter choice : ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            
            break
        elif choice == '5':
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))

            print("Result:", power(num1, num2))

            break
        elif choice in ('6', '7', '8'):
            try:
                matrix1 = np.array(eval(input("Enter first matrix (as a 2D list): ")))
                matrix2 = np.array(eval(input("Enter second matrix (as a 2D list): ")))

                if choice == '6':
                    print("Result:\n", matrix_add(matrix1, matrix2))
                elif choice == '7':
                    print("Result:\n", matrix_subtract(matrix1, matrix2))
                elif choice == '8':
                    print("Result:\n", matrix_multiply(matrix1, matrix2))
                
                break
            except (SyntaxError, NameError):
                print("Invalid input. Please enter matrices in the correct format.")
        else:
            print("Invalid input. Please try again.")

except KeyboardInterrupt:
    print("\nCalculator program interrupted. Exiting...")
