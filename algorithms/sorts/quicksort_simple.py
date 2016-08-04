# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:23:02 2016

@author: Aaron Beckett
"""

def quicksort(A):
    """
    Sorts A in ascending order using a simple implementation of quicksort
    
    Quicksort is usually UNSTABLE, NOT ADAPTIVE, OFFLINE
    
    This version performs worst case when there are many repeated elements
    or when sorting already sorted lists.
    
    Time complexity :
        Worst  : O(N^2)
        Average: O(N logN)
        Best   : O(N logN)
    Space complexity: O(logN) auxiliary
    """
    
    def swap(a, b):
        """Swap elements at indices a and b"""
        temp = A[a]
        A[a] = A[b]
        A[b] = temp
    
    def partition(lo, hi):
        """
        Partition array around a pivot then return the index of that pivot
        
        Elements less than the pivot will be to the left of the pivot,
        elements greater than the pivot will be to the right.
        """
        # Set pivot to furthest left element
        pivot = A[lo]
        # Initialize i and j to just off either end of the remaining elements
        i = lo + 1
        j = hi
        
        # Partition elements based on the pivot
        while True:
            while i <= hi and A[i] < pivot: i += 1
            while j >= lo and A[j] > pivot: j -= 1
            if i >= j:
                break
            swap(i, j)
            
        # Swap the pivot with A[j], which is the furthest right element
        # that is less than the pivot
        swap(lo, j)
        
        # Return the location of the pivot
        return j
            
    def sort_section(lo, hi):
        """Sort array between lo and hi"""
        if lo < hi:
            p = partition(lo, hi)
            
            # As suggested by Robert Sedgewick, recurse into the smaller
            # partition first to ensure no worse than O(logN) space complexity
            if p - lo < hi - p:
                sort_section(lo, p-1)
                sort_section(p+1, hi)
            else:
                sort_section(p+1, hi)
                sort_section(lo, p-1)
         
    # Start recursively sorting array
    sort_section(0, len(A)-1)
    