#!/usr/bin/env python3

try:
    with open("filename.txt", "w") as file:
        data = file.write("i understood file management and exception handling")
        print(file)
except FileNotFoundError:
    print("file not found")

finally:
    #file.close()
    pass