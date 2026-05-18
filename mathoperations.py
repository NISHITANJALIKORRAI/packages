import math


#input from user
n=float(input("Enter a number: "))


print("\n--------MATH OPERATIONS--------")


#Square Root
if n>=0:
    print("Square Root of n=",math.sqrt(n))
else:
    print("Square Root is not possible for negative numbers")


#Power
print("Square of n=",math.pow(n,2))


#Asolute Value
print("Asolute Value of n=",math.fabs(n))


#Ceiling Value
print("Ceiling value for 5.4=",math.ceil(5.4))


#Floor Value
print("Floor value for 5.4=",math.floor(5.4))


#Trignomertic Functions
print("Sine Value=",math.sin(n))
print("Cosine Value=",math.cos(n))
print("Tangent Value=",math.tan(n))


#Logarithm
if n>0:
    print("Log Value of n=",math.log(n))
else:
    print("Logarithm is not possible for negative numbers")


#Factorial
if n>0 and n.is_integer():
    print("Factorial of n=",math.factorial(int(n)))
else:
    print("Factorial is not possible for negative numbers or floating numbers")