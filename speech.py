# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:00:10 2022

@author: dhung


a=input("one num")
b=input("another num")
c= None
d= None
if(a>b):
    print(a,"is greater")
    c=float(a)-float(b)
    print(b,"is smaller than ", a ,"by",c)
else:
    print(b," is greater")  
    d=float(b)-float(a)
    print(a,"is smaller than", b , "by",d)
    
    print(99.98+0.009999999999990905)


print("another one")
e=input("num")
e=int(e)

if(e==0):
    print("Zero")
else:
    print("non zero")
a=input("ENTER NUM(0-9)")
a=int(a)
if a==0:
    print("zero")
elif a==1:
    print("one")
elif a==2:
    print("two")
elif a==3:
    print("three")
elif a==4:
    print("four")
elif a==5:
    print("five")
elif a==6:
    print("six")
elif a==7:
    print("seven")
elif a==8:
    print("eight")
elif a==9:
    print("nine")
else:
    print("invalid")
#wap which accepts numb and print weekday
wk=input("enter number of weekday ")
if wk=="1":
   result="The day is sunday"
elif wk=="2":
   result="The day is monday"
elif wk=="3":
   result="The day is tuesday"
elif wk=="4":
   result="The day is wednesday"
elif wk=="5":
   result="The day is thurday"
elif wk=="6":
  result="The day is friday"
elif wk=="7":
   result="The day is saturday"
else:
    result="invalid input"
print(result)
n3= None
n=input("enter a num")
n1=input("enter another num")
n2=input("enter another num")
if(n>n1 and n>n2):
    n3=n
elif(n1>n and n1>n2):
    n3=n1
elif(n2>n and n2>n1):
        n3=n2
elif(n == n1 == n2):
    print("enter different numbers")
if n3!= None: 
    print("greatest num=",n3)
    
"""
    import sys
    
    
n=input("enter a number")
n=int(n)
n1=input("enter another number")
n1=int(n1)
print("1.add--2.difference--3.multiplication--4.division--5.rem--6.exit ")
n2=input("enter a choice")
n2=int(n2)
if n2==1:
    ok=n+n1
elif n2==2:
    ok=n-n1
elif n2==3:
    ok=n*n1
elif n2==4:
    ok=n/n1
elif n2==5:
    ok=n%n1
elif n2==6:
   ok=None
else:
    print("invalid input")
if ok != None:
   print("result=", ok)
else: 
    print("exited the program")

    
#9851-141514






      

