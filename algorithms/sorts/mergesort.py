# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:39:35 2016

@author: Aaron Beckett
"""

def mergesort(A):
    """
    Sorts A in ascending order using bottom up merge sort
    
    Merge sort is STABLE, NOT ADAPTIVE, ONLINE
    
    Time complexity :
        Worst  : O(N logN)
        Average: O(N logN)
        Best   : O(N logN)
    Space complexity: O(N) auxiliary
    """
    
    def merge(left, right, end, B):
        """Merge two sorted arrays in to one sorted array"""
        # left run : A[left:right]
        # right run: A[right:end]
        i = left
        j = right
        # While there are elements in the left or right runs...
        for k in range(left, end):
            if i < right and (j >= end or A[i] <= A[j]):
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                j += 1

    # Store size and id of A    
    N = len(A)
    address = id(A)
            
    # Initialize workspace array
    B = [None] * N

    # Each 1-element run in A is already sorted
    # Make successively longer sorted runs
    width = 1
    while width < N:
        # Array A is full of runs of length width
        for i in range(0, N, 2*width):
            # Merge two runs: A[i:i+width-1] and A[i+width:i+2*width-1] to B[]
            # or copy A[i:n-1] to B[] ( if(i+width >= n) )
            merge(i, min(i+width, N), min(i + 2*width, N), B)
            
        # Now workspace B is full of runs of length 2*width
        # Swap A and B
        temp = A
        A = B
        B = temp
        
        # Increase width
        width *= 2
        
    # Make sure the sorted array is located at the correct address
    if id(A) != address:
        for i in range(N):
            B[i] = A[i]
