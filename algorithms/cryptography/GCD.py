# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 15:38:43 2016

@author: Aaron Beckett
"""

def gcd(A, B):
    """
    Calculate greatest common divisor of A and B
    """
    
    if A == 0:
        # gcd(0, B) = B
        return B
    elif B == 0:
        # gcd(A, 0) = A
        return A
    else:
        # If
        #   A = B*Q + R
        # where Q is an integer and R <= B-1,
        # then
        #   gcd(A, B) = gcd(B, R)
        R = A % B
        return gcd(B, R)