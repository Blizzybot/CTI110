#Terry Norman
#02/26/2026
#P1HW1
#This program collects information from users, and displays it back to the user.
print("----- Calculating Exponents -----")

base = int(input("Enter an integer for the base value: "))
exponent = int(input("Enter an integer for the exponent value: "))
result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result}")

print("\n----- Adding and Subtracting -----")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_two = num1 + num2

final_result = sum_two - num3
print(num1, "+", num2, "-", num3, "is", final_result)
