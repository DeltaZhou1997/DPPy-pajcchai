#!/usr/bin/python3

firstNum = int(input("Give me the first number: "))
secondNum = int(input("Give me the second number: "))

print("Thank you!")

print(f"{firstNum} + {secondNum} = {firstNum + secondNum}")
print(f"{firstNum} - {secondNum} = {firstNum - secondNum}")

if secondNum != 0:
    print(f"{firstNum} / {secondNum} = {int(firstNum / secondNum)}")
else:
    print(f"{firstNum} / {secondNum} = Error (Division by zero)")

print(f"{firstNum} * {secondNum} = {firstNum * secondNum}")