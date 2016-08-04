# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 20:30:31 2016

@author: Aaron Beckett
"""

def bubble_sort(A):
    """
    Sorts A in ascending order using an optimized bubble sort
    
    Time complexity :
        Worst  : O(N^2)
        Average: O(N^2)
        Best   : O(N)
    Space complexity: O(1) auxiliary
    """
    
    def swap(a, b):
        """Swap elements at indices a and b"""
        temp = A[a]
        A[a] = A[b]
        A[b] = temp
        
    # Sort A by passing over and comparing pairs until there are no more swaps
    n = len(A)
    while n != 0:
        newn = 0
        for i in range(1,n):
            if A[i-1] > A[i]:
                swap(i-1, i)
                newn = i
        n = newn # There is no need to re-check pairs after the last swap