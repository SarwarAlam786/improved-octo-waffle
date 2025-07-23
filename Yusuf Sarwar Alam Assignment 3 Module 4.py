#Task 1: Calculate Factorial Using a Function
#1.Using a For Loop:
'''

num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    i=i+1
print("Factorial of ",num,'is',fact)
'''

#2 Using a While Loop:

'''
num=int(input("Enter a number: "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("Factorial of ",num,'is',fact)
'''
# Using Recursion:
'''
n=int(input("Enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
Result=factorial(n)
print("Factorial of", n, "is ",Result)
'''
#Task 2: Using the Math Module for Calculations
'''
n=int(input("Enter a number: "))
from math import *
print("Squareroot:",sqrt(n))
print("Logarithem:",log(n,e))
print("Sine:",sin(n))
'''
