# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 06:24:05 2022

@author: dhung


wk=input("enter number of weekday ")
wk= int(wk)
match wk:
    
    case 1:
        result="The day is sunday"
    case 2:
            result="The day is monday"
    case 3:
        result="The day is tuesday"
    case 4:
        result="The day is wednesday"
    case 5:
        result="The day is thurday"
    case 6:
        result="The day is friday"
    case 7:
        result="The day is saturday"
if wk>7:
    result="invalid input"
print(result)

print("broadways")
print("broadways")
print("broadways")
print("broadways")
print("broadways")

start= None
stop= None

start= 1
value=input("what do you want to print")
stop= input("enter no. of times to print")
stop= int(stop)
while start<= stop:
    print(value)
    start +=1
"""

a=input("enter start no.")
b=input("enter stop no.")
a= int(a)
b= int(b)
sum=1
while a<= b:
    sum=a+1
print(sum)




