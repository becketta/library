# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:09:51 2016

@author: Aaron Beckett
"""

import math

def min_squares(N):
    """
    Find minimum number of square areas that will fill an area of size N
    
    Time complexity : O(N logN) ??
    Space complexity: O(N)
    """
    
    # Save already computed answers (memoize)
    cache = [None] * (N+1)
    cache[0] = 0
    cache[1] = 1
    
    # Iterate through valid starting sizes, recursively
    # solving the remainders
    def min_pads(n):
        # If we've already computed this answer
        if cache[n] is not None:
            return cache[n]   # Return memoized answer
        
        # Otherwise calulate it
        mn = math.inf           # Keep track of min so far
        i = int(math.sqrt(n))   # Largest square possible for n
        while i > 0:            # It. through each square
            r = n - i*i         # Calc remainder for this square
            a = 1 + min_pads(r) # Recursively find answer
            if a < mn:          # Update min if needed
                mn = a
            i -= 1
                
        # Save result in cache and return min
        cache[n] = mn
        return mn
    
    return min_pads(N)
