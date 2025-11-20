#!/usr/bin/python3

x = 0
y = 0
result = []

while x <= 10:
    while y <= 10:
        result.append(x * y)
        y += 1
    print(f"Table of {x}:", *result)
    result.clear()
    y = 0
    x += 1
