"""
********************************************************************************
* Project Name:  FizzBuzz
* Description:   This project is implementation of fizzbuzz with user input
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

print("Welcome to FizzBuzz Generator!")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
for i in range(1, 101):
    if i % first == 0 and i % second == 0:
        print("FizzBuzz")
    elif i % first == 0:
        print("Fizz")
    elif i % second == 0:
        print("Buzz")
    else:
        print(i)