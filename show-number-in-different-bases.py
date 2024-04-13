#!/bin/python3

def num_char(n):
	l = ["0","1","2","3","4","5","6","7","8","9",
	"a","b","c","d","e","f","g","h","i","j",
	"k","l","m","n","o","p","q","r","s","t",
	"u","v","w","x","y","z"]

	return l[n]

def sum_list(l):
	ss =""
	for s in l:
		ss=ss+s
	return ss

vv=int(input("Please input a natural number:"))

for b in range(2,36):
	v=vv
	r=[""];

	while v != 0:
		m=v%b
		v=int(v/b)
		r.insert(0, num_char(m))

	print("In base", b, ":", vv,"in decimal is expressed as","`", sum_list(r), "`.")

