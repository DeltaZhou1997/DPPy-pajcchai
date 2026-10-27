#!/usr/bin/python3

numberMulti = int(input("Enter a number\n"))

i=0
while i<10:
    result = i*numberMulti
    #print(str(i)+"x"+str(numberMulti)+"="+str(result))
    print(f"{i} x {numberMulti} = {result}")
    i+=1