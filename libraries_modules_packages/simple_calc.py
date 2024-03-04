# Mini-calculator
import math_operations

print("We are going to add two numbers...")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = math_operations.add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")


print("We are going to substract two numbers...")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = math_operations.substract(first_num, second_num)
print(f"{first_num} - {second_num} = {result}")


print("We are going to multiply two numbers...")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = math_operations.multiply(first_num, second_num)
print(f"{first_num} * {second_num} = {result}")


print("We are going to divide two numbers...")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = math_operations.divide(first_num, second_num)
print(f"{first_num} / {second_num} = {result}")

