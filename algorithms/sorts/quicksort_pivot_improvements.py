# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:23:02 2016

@author: Aaron Beckett
"""

from random import randint

def leftmost(lo, hi):
    """Select the leftmost index as the pivot"""
    return lo
    
def random(lo, hi):
    """Select a random index for the pivot"""
    return randint(lo, hi)

def median(lo, hi):
    """
    Select the median element as the pivot

    To avoid integer overflow, naive calulation of the median:
        (lo + hi) / 2
    is not used.
    """
    return lo + (hi - lo) // 2
    
def med3(a, b, c):
    """Return the median of three numbers"""
    if (a <= b or a <= c) and (a >= b or a >= c):
        return a
    elif (b <= a or b <= c) and (b >= a or b >= c):
        return b
    else:
        return c

def median_of_three(lo, hi):
    """
    Select pivot using the median-of-three rule
    
    Median-of-three is a good strategy for larger partitions.
    """
    med = median(lo, hi)
    return med3(lo, med, hi)
    
def ninther(lo, hi):
    """
    Select pivot using the recursive median-of-three rule
    
    Using the ninther as pivot is a good strategy for very large partitions.
    """
    diff = (hi - lo) // 3
    m1 = lo + diff
    m2 = m1 + diff
    return med3(median_of_three(lo, m1), median_of_three(m1, m2), median_of_three(m2, hi))

def quicksort(A, select_pivot = leftmost):
    """
    Sorts A in ascending order using a simple implementation of quicksort
    
    This version fixes issues with sorting already sorted arrays by using
    more advanced pivot selection techniques.
    
    Time complexity :
        Worst  : O(N^2)      When array contains mostly the same element
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
        # Swap the pivot with the left-most element
        swap(lo, select_pivot(lo, hi))
        pivot = A[lo]
        # Initialize i and j to either end of the remaining elements
        i = lo + 1
        j = hi
        
        # Partition elements based on the pivot
        while True:
            while i <= hi and A[i] < pivot: i += 1
            while j >= lo and A[j] > pivot: j -= 1
            if i >= j:
                break
            swap(i, j)
            
        # Swap the pivot with A[j] which is the furthest right element that is
        # less than the pivot
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
    