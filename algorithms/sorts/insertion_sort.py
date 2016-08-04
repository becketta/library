# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:39:51 2016

@author: Aaron Beckett
"""

def insertion_sort(A):
    """
    Sorts A in ascending order using insertion sort
    
    Insertion sort is STABLE, ONLINE, ADAPTIVE
    
    Time complexity :
        Worst  : O(N^2), O(N*k) when each element is no more than k
                                spaces away from its sorted position
        Average: O(N^2)
        Best   : O(N)
    Space complexity: O(1) auxiliary
    """
    
    def shift_right(a):
        """Shift element at index a to the right one space"""
        A[a+1] = A[a]
        
    # Sort A by gradually building sorted list where the first i+1 elements
    # are always sorted, forming a partial result, at the start of a loop
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while A[j] > x:
            shift_right(j)
            j -= 1
        A[j+1] = x