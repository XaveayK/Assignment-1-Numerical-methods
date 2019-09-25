# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:39:34 2019

@author: 3063475 Xavier Kidston, 399, Ron Meleshko
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
"""
Purpose: To be non-robust and instead the naive solution
"""
def onepointonefiveNotRobust(vector):
    summ = 0
    for x in vector:
        summ += x**2 #This isn't effected by 0's
    try:
        return summ**(1/2)
    except:
        return "Overflow or underflow would occur"
"""
Purpose: This is the robust implementation, that's just straight up better in every way
"""
def onepointonefive(vector): 
    l1 = []
    summ = Decimal('0')
    for x in vector:
        l1.append(Decimal(int(x)))
    for x in l1:
        summ += x**2
    return summ.sqrt()
#def onepointonefivel1(vector): return np.linalg.norm(vector, 1)
#def onepointonefivelinf(vector): return np.linalg.norm(vector, np.inf)


if __name__ == '__main__':
    
    #Calls the 1.1 in computing
    onepointone()
    print("Absolute error gets larger, the relative error shrinks\n\n")
    #Calls each of the values for 1.10 in computing
    print(onepointonezero(6.0, 5.0, -4.0))
    print(onepointonezero(6.0*(10.0**154.0), 5.0*(10.0**154.0), -4.0*(10.0**154.0)))
    print(onepointonezero(0.0, 1.0, 1.0))
    print(onepointonezero(1.0, -10.0**5.0, 1.0))
    print(onepointonezero(1.0, -4.0, 3.999999))
    print(onepointonezero(10.0**-155.0, -10.0**155.0, 10.0**155.0))
    #Calls for 1.15
    a = np.array([1,2,3,4,5])
    b = np.array([5,0,55,10**155,5])
    c = np.array([0,0,10**156,0])
    d = np.array([0, 10**-156, 3**-178])
    print("\n\nAll values are for the vector x1=[1,2,3,4,5]")
    print("\n1.10 Robust:")
    print("Euclidean Norm robust:", onepointonefive(a))
    print("\n1.10 non-robust:")
    print("Euclidean Norm non-robust:", onepointonefiveNotRobust(a))
    print("For this case there is no difference, but the robust version does take more computation.")
    
    print("\n\nAll values are for the vector x2=[5,0,55,10**155,5]")
    print("\n1.10 Robust:")
    print("Euclidean Norm robust:", onepointonefive(b))
    print("\n1.10 non-robust:")
    print("Euclidean Norm non-robust:", onepointonefiveNotRobust(b))
    print("For this case the naive solution outputs an overflow.")

    print("\n\nAll values are for the vector x2=[0,0,10**156,0]")
    print("\n1.10 Robust:")
    print("Euclidean Norm robust:", onepointonefive(c))
    print("\n1.10 non-robust:")
    print("Euclidean Norm non-robust:", onepointonefiveNotRobust(c))
    print("For this case the naive solution outputs an overflow.")
    
    print("\n\nAll values are for the vector x2=[0,0,10**156,0]")
    print("\n1.10 Robust:")
    print("Euclidean Norm robust:", onepointonefive(d))
    print("\n1.10 non-robust:")
    print("Euclidean Norm non-robust:", onepointonefiveNotRobust(d))
    print("For this case the naive solution outputs an underflow.")
    