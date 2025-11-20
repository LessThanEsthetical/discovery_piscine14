#!/usr/bin/python3

x = int(input("Enter a number less than 25: "))

if x >= 25:
    print("Error")
else:
    while x < 25:
        x += 1
        print("Inside the loop, my variable is", x)
