# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:32:20 2016

@author: Aaron Beckett
"""

def mrh(height):
    """
    Finds maximum area of rectangle made from histogram heights
    """
    
    N = len(height)
    width = [1] * N
    
    # Calculate left widths
    left = []
    for i in range(N):
        # Remove from left all buildings taller than or equal to current
        while left and height[i] <= height[left[-1]]:
            left.pop()
    
        if not left:
            # All buildings to the left are taller
            width[i] += i
        else:
            # Top of left stack is the nearest shorter buliding to left
            width[i] += i - (left[-1] + 1)
        
        # Add current building to the stack
        left.append(i)

    # Calculate right widths
    right = []
    for i in reversed(range(N)):
        # Remove from right all buildings taller than or equal to current
        while right and height[i] <= height[right[-1]]:
            right.pop()
    
        if not right:
            # All buildings to the right are taller
            width[i] += (N-1) - i
        else:
            # Top of right stack is nearest shorter building to the right
            width[i] += (right[-1] - 1) - i
    
        # Add current building to the stack
        right.append(i)

    # Calculate max
    mx = 0
    for i in range(N):
        mx = max(mx, width[i] * height[i])
    
    return mx