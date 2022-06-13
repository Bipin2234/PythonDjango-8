# -*- coding: utf-8 -*-
"""
Created on Tue May 31 06:18:29 2022

@author: dhung

var1= None
var2=None
v3= None
v4=None
v5= None
v6= None

var1=input("num")
var2=input("numm")
var1=int(var1)
var2=int(var2)
print("first no.{}".format(var1))
print("second no.{}".format(var2))
v3=var1+var2
v4= var1-var2
v5=var1*var2
v6=var1/var2
print("sum=",v3)
print("diff=",v4)
print("multiplication=",v5)
print("division",v6)
[][][][][][][[[[]]]][][][][][][][][][][[[[[[[[[[[[[[[[[]][[]][[]]]]]]]]]]]]]]]]]
r1= True
r2= False
r3= r1 and r2
r4= r2 or r3
print(r3)
print( not r4)
"""

from array import array

nums=array('i',[6,7,8,9,4])
print(nums)
print(nums[3])
no=array('i',[76,43,23,56])
no[2]=99
print("total=",no[0]+no[1]+no[2]+no[3])
print("average=",(no[0]+no[1]+no[2]+no[3])/5)
print(max(no))

class student:
    pass
s1=student()
print(type(s1))





