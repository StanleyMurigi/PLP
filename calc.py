#!/usr/bin/env python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    a = float(input("Enter the first number for mathematical operation: "))
    b = float(input("Enter the second number for mathematical operation: "))
    sign = input("Enter the operation sign to be used: ")

    if sign == "+":
        result = add(a, b)
        print(f'{a} {sign} {b} = {result}')

    elif sign == "-":
        result = sub(a, b)
        print(f'{a} {sign} {b} = {result}')

    elif sign == "*":
        result = mul(a, b)
        print(f'{a} {sign} {b} = {result}')

    elif sign == "/":
        result = div(a, b) if b != 0 else "Error of division by zero"
        print(f'{a} {sign} {b} = {result}')
    else:
        print("Invalid character")
    

if __name__ == "__main__":
    main()