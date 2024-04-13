#!/bin/python3

m = 0
while m <= 0:
	m=int(input("Please input a positive integer:"))
a=1
b=1
x=float(a+b)

#print(a,"/", b)
#print("/")
#print(b)



while x<int(m):
	print(int(a)," / ", int(b),": ",a/b)
	x=a+b
	a=b
	b=x


