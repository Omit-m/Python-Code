import math

a= int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
d=(b*b) -(4*a*c)

if d==0:
	x = (-b/(2*a))
	print("roots are real & eqial & are:",x,7)

elif d>0 :
	x1=(-b+math.sqrt(d))/(2*a)
	x2=(-b-math.sqrt(d))/(2*a)
	print("root are the real & unwqual & are:",x1,x2)
else:
	print("the roots are imaginary")
