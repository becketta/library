# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:23:02 2016

@author: Aaron Beckett
"""

def quicksort(A):
    """
    Sorts A in ascending order using an implementation of quicksort with
    Dutch National Flag partitioning.
    
    This version fixes issues with repeated elements by sorting all elements
    equal to the pivot into their final places before recursively sorting
    the subarrays.
    
    Time complexity :
        Worst  : O(N^2)      When array is already sorted
        Average: O(N logN)
        Best   : O(1)        When each element is the same
    Space complexity: O(logN) auxiliary
    """
    
    def swap(a, b):
        """Swap elements at indices a and b"""
        temp = A[a]
        A[a] = A[b]
        A[b] = temp
    
    def partition(pivot, lo, hi):
        """
        Partition array around a pivot, with elements equal to the pivot correctly
        placed, then return the locations before and after the pivot elements.
        """
        # Initialize i, j, and n
        #
        # i holds the boundary for numbers lesser than pivot (A[i-1] != pivot)
        # j is the number under consideration
        # n holds the boundary for numbers greater than pivot (A[n+1] != pivot)
        i = lo
        j = lo
        n = hi
        
        # Partition elements based on the pivot
        while j <= n:
            if A[j] < pivot:
                swap(i, j)
                i += 1
                j += 1
            elif A[j] > pivot:
                swap(j, n)
                n -= 1
            else:
                j += 1
        
        # Return the locations before and after elements equal to the pivot
        return i, n
            
    def sort_section(lo, hi):
        """Sort array between lo and hi"""
        if lo < hi:
            p = A[lo]
            left, right = partition(p, lo, hi)
            
            # As suggested by Robert Sedgewick, recurse into the smaller
            # partition first to ensure no worse than O(logN) space complexity
            if left - lo < hi - right:
                sort_section(lo, left-1)
                sort_section(right+1, hi)
            else:
                sort_section(right+1, hi)
                sort_section(lo, left-1)
    
    # Start recursively sorting array     
    sort_section(0, len(A)-1)
    