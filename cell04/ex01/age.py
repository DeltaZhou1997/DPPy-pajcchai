#!/usr/bin/python3

def future_age(age):
    print(f"You are currently {age} years old.")
    for years in range(10, 31, 10):
        print(f"In {years} years, you'll be {age+years}.")

ageInput = int(input("Please tell me your age: "))
future_age(ageInput)