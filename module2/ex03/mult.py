#!/usr/bin/python3

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
mult = x * y

print(f"{x} x {y} = {mult}")
if mult > 0:
    print("The result is positive.")
elif mult < 0:
    print("The result is negative.")
elif mult == 0:
    print("The result is positive and negative.")
