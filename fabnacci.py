#!/bin/python3

m=input("please input maxnum:")

a=1
b=1
x=0
print(1)
print(1)
while x<int(m):
    x=a+b
    a=b
    b=x
    if x<int(m):
        print(x)


