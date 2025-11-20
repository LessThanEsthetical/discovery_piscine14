#!/usr/bin/python3

x = int(input("Please tell me your age: "))
print(f"You are currently {x} years.")

for i in range(10, 40, 10):
  print(f"In {i} years, you'll be {x + i} years old.")
