#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345" :
        return "Access granted"
    return "Access denied"

    

def hows_the_weather(temperature):
    if temperature <= 33 :
        return "It's brisk out there!"
    if temperature <= 55 :
        return "It's a little chilly out there!"
    if temperature <= 75 :
        return "It's perfect out there!"
    if temperature <= 99 :
        return "It's too dang hot out there!"
    
    return 

def fizzbuzz(num):
    if num%3 == 0 and num%5 == 0: 
      return   "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 ==0:
        return "Buzz"
    return num
# If the operation is one of the following: `+`, `-`, `*`, or `/`, return
# the value of calling the operation on the two numbers.

# Otherwise, output a
# message saying "Invalid operation!" and  return `None`
def calculator(operation, num1, num2):
    if operation == "+": 
        addi = add(num1,num2)
        return addi
    if operation == "-": 
        subt = sub(num1, num2)
        return subt
    if operation == "*": 
        mul = multi(num1,num2)
        return mul
    if operation == "/":
        divi = div(num1,num2)
        return divi
    return print("Invalid operation!")

def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def multi(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1/num2
