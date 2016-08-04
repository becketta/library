# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:22:16 2016

@author: Aaron Beckett
"""

def answer(heights):
    """
    Calculate volume of water on top of hutches
    
    It's raining on hutches of different heights, some water won't run off
    
    ...X...
    .XOX...
    .XOXOOX
    .XXXOXX
    XXXXXXX
    1425123
    
    If 'X' is part of a hutch and 'O' is water, calulate the number of 'O's
    
    Time complexity : O(N)
    Space complexity: O(N)
    """
    
    N = len(heights)    # Number of hutches
    mx_left = 0         # Current tallest hutch to left
    mx_right = 0        # Current tallest hutch to right
    left = [None] * N   # Tallest hutch to left for each
    right = [None] * N  # Tallest hutch to right for each
    
    # Find largest hutches to the left and right of
    # each individual hutch
    for i in range(N):
        if heights[i] > mx_left:
            # Taller than all to left, this is new max
            mx_left = heights[i]
        else:
            left[i] = mx_left
            
        if heights[N-i-1] > mx_right:
            # Taller than all to right, this is new max
            mx_right = heights[N-i-1]
        else:
            right[N-i-1] = mx_right
            
    # Calculate volume of water by calculating amount on top of each hutch
    water = 0
    for i in range(N):
        if left[i] and right[i]:
            # There are taller hutches to the left and right
            # therefore there will be water on top
            h = min(left[i], right[i])
            water += h - heights[i]
            
    return water