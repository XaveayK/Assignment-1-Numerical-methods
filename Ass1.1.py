# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:39:34 2019

@author: kidst
"""
import numpy as np
from decimal import *
getcontext().prec = 10


"""
Purpose: To calculate the n factorial approximate and output its absolute error and relative error
"""
def onepointone():
    for i in range(1, 11, 1):
        approx = np.math.factorial(i)
        fact = np.sqrt(2 * np.pi * i) * np.power((i / np.exp(1)), i)
        absE = abs(approx - fact)
        print("n=" + str(i), "Absolute Error:", absE, end = "")
        print("\t\tRelative Error:", absE / fact)
    return

"""
Purpose: To calculate the roots most effectively given the numpy library
@Params: a - the first term in the poly
         b - the second term in the poly
         c - the third term in the poly
@Return: [x1, x2] where both are the zero's of the equation
         x where only one intercept exists
"""
def onepointonezero(a, b, c):
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    if a == 0: return Decimal(-c / b) #Handles y = mx+b
    else:
        bsq = Decimal.sqrt(b**2 - 4 * a * c)    
        x1 = (-b + bsq) / (2*a)
        x2 = (-b - bsq) / (2*a)
    return (x1, x2)

def onepointonefive(vector): return np.linalg.norm(vector)
def onepointonefivel1(vector): return np.linalg.norm(vector, 1)
def onepointonefivelinf(vector): return np.linalg.norm(vector, np.inf)


if __name__ == '__main__':
    
    #Calls the 1.1 in computing
    onepointone()
    print("Absolute error gets larger, the relative error shrinks")
    print()
    print()
    #Calls each of the values for 1.10 in computing
    print(onepointonezero(6.0, 5.0, -4.0))
    print(onepointonezero(6.0*(10.0**154.0), 5.0*(10.0**154.0), -4.0*(10.0**154.0)))
    print(onepointonezero(0.0, 1.0, 1.0))
    print(onepointonezero(1.0, -10.0**5.0, 1.0))
    print(onepointonezero(1.0, -4.0, 3.999999))
    print(onepointonezero(10.0**-155.0, -10.0**155.0, 10.0**155.0))
    #Calls for 1.15
    x = np.array([1,2,3,4,5])
    print()
    print()
    print("All values are for the vector x1=[1,2,3,4,5]")
    print()
    print(onepointonefive(x))
    print(onepointonefivel1(x))
    print(onepointonefivelinf(x))
    print()
    print("Euclidean norm through numpy is more efficient than its alternatives and arguably more useful than its counterparts.")
    print("The set back to Euclidean norm is that it takes a lot more space than its counterparts."
