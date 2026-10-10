import math 
a=int(input("enter the opposite side of the angle in a triangle"))
b=int(input("enter the adjacent side "))
c=math.sqrt(a**2+b**2)
print("hypotenuse is ",c)
print("sin=",(a/c))
print("cos=",(b/c))
print("tan=",(a/b))
