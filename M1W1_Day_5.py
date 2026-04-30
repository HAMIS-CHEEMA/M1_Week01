import math
# calculator
print("=" * 50)
print("Calculator".center(50))
print("=" * 50)

while True:
    print("\n Menu")
    print("1. Arithmetic operations")
    print("2. pi calculations")
    print("3. Exit")

    choice = input("\n enter your choice(1-3): ")
    # Arithmetic Operations
    if choice == "1":
        print("\nbasic_arithmetic")
        a = float(input("enter 1st num: "))
        b = float(input("enter 2nd num: "))

        sum_results = a + b
        subtraction = a - b
        mul = a * b

        print("\n Results")
        print(f"(Addition) {a} + {b} = {sum_results}")
        print(f"(Subtraction) {a} - {b} = {subtraction}")
        print(f"(Multiplication) {a} * {b} = {mul}")

        if b != 0:
            division = a / b
            modulus = a % b
            print(f"(Division) {a} / {b} = {division}")
            print(f"(Remainder) {a} % {b} = {modulus}")
        else:
            print("denominator cannot be zero")

        #power / exponent
        exponent_power = float(input(f"enter power of {a} ^ ?"))
        exponent_results = a ** exponent_power
        print(f"{a} ^ {exponent_power} = {exponent_results}")

    # pi calculations
    elif choice == "2":
        print("=" * 50)
        print("\n pi calculation".center(50))
        print("=" * 50)
        c = float(input("enter multiplier for pi: "))
        pi_value = math.pi
        calc_pi  = c * pi_value

        print("\n Results")

        print(f"the value of pi with multiplier is = {calc_pi:.8f}")
        # circle calculation
        radius = float(input("\nEnter the radius for circle: "))
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2
        print(f"Circumference = {circumference}")
        print(f"Area = {area}")
        #Exit
    elif choice == "3":
        print("\n Thanks for using this calculator ! GoodBye!")
        break
    else:
        print("\n Invalid choice Please enter 1,2,3...")

    #Ask to continue
    continue_choice = input("do you want to continue (yes/no) ? ").lower()
    if continue_choice != "yes":
        print("goodbye")
        break

print("\n" + "=" * 50)
#===================================================================================
















