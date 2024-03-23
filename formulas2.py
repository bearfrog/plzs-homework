#!/bin/python3

def area_of_square(a):
    return a ** 2

def area_of_rectangle(a,b):
    return a * b

def area_of_triangle(a,h):
    return a * h / 2

a=input("please input the shape:")
if int(a)==0:
    l=input("please input length:")
    s=area_of_square(int(l))
    print("area of square:",s)
elif int(a)==1:
    l=input("please input length:")
    w=input("please input width:")
    s=area_of_rectangle(int(l),int(w))
    print("area of rectangle:",s)

elif int(a)==2:
    l=input("piease input length:")
    o=input("piease input height:")
    s=area_of_triangle(int(l),int(o))
    print("area of rectangle:",s)

else:
    print("wrong")



