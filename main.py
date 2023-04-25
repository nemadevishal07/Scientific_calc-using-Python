""" Unlike basic calculators that can only handle smaller values, a scientific calculator can handle numbers on a much vaster scale, 
which can be useful when it comes to collecting data or working as a physicist or chemist. It can also calculate negative scientific notation. """

import math

print("Scientific Calculator")

while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponent")
    print("7. Logarithm")
    print("8. Trigonometric Functions")
    print("9. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == 2:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    elif choice == 3:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    elif choice == 4:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            print("Result:", num1 / num2)

    elif choice == 5:
        num = float(input("\nEnter a number: "))
        if num < 0:
            print("Error: cannot take square root of a negative number")
        else:
            print("Result:", math.sqrt(num))

    elif choice == 6:
        base = float(input("\nEnter the base: "))
        exponent = float(input("Enter the exponent: "))
        print("Result:", base ** exponent)

    elif choice == 7:
        num = float(input("\nEnter a number: "))
        if num <= 0:
            print("Error: logarithm of a non-positive number")
        else:
            base = float(input("Enter the base: "))
            print("Result:", math.log(num, base))

    elif choice == 8:
        angle = float(input("\nEnter the angle (in degrees): "))
        print("Trigonometric Functions:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        trig_choice = int(input("Enter your choice: "))
        if trig_choice == 1:
            print("Result:", math.sin(math.radians(angle)))
        elif trig_choice == 2:
            print("Result:", math.cos(math.radians(angle)))
        elif trig_choice == 3:
            print("Result:", math.tan(math.radians(angle)))
        else:
            print("Error: invalid choice")

    elif choice == 9:
        print("\nExiting the program...")
        break

    else:
        print("Error: invalid choice")
