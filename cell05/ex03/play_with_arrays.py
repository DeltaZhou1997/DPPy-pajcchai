#!/usr/bin/env python3

oriArray =  [2, 8, 9, 48, 8, 22, -12, 2]
newArray = [x+2 for x in oriArray if x > 5]

print(oriArray)
print(set(newArray))