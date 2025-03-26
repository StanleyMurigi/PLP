#!/usr/bin/env python3

def calculate_discount(price, discount_percent):
    new_price = [price - (price * discount_percent/100) if discount_percent >= 20  else price]
    return new_price


if __name__ == "__main__":
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    print(calculate_discount(price, discount_percent))
