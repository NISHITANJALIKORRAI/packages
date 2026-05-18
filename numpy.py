import numpy as np

a=np.array([10,30,20,40])
b=np.array([1,3,2,4])


#Display Array
print("Array a=",a)
print("array b=",b)


print("---Arithematic Operations---")
print("Addition=",a+b)
print("Subtraction=",a-b)
print("Multiplication=",a*b)
print("Division=",a/b)
print("Modules=",a%b)
print("Square of a=",np.pow(a,2))
print("Square root of a=",np.sqrt(a))
print("\n")


#Maximam Value
print("Maximum Value of a=",np.max(a))
#Minimum Value
print("Minimum Value of a=",np.min(a))
print("\n")


#Sum of elements
print("Sum of elements in a=",np.sum(a))
print("\n")


print("---Statistical Operators---")
print("Mean of a=",np.mean(a))
print("Median of a=",np.median(a))
print("Standard Deviation of a=",np.std(a))
print("\n")


#Sorting
print("Sorted Array a=",np.sort(a))
print("\n")


#Reshape
c=np.array([1,2,3,4,5,6])
print("Array c=",c)
print("Reshaping array c\n",c.reshape(2,3))
print("\n")


print("---Matrix Operations---")
#2D array
d=np.array([[1,2],[3,4]])
print("2D Matrix\n",d)
print("Transpose Matrix\n",d.T)
print("Matrix Addition\n",d+d)
print("Matrix Multiplication\n",np.dot(d,d))
print("\n")


#Indexing
print("First Index of a=",a[0])
print("\n")


#Slicing
print("Sliced elements of a=",a[1:3])