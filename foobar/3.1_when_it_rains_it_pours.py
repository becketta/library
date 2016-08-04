# -*- coding: utf-8 -*-
"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where
the captive rabbits are being held, but a sudden storm puts your escape plans at
risk.

The structural integrity of the rabbit hutches you've built to house the
fugitive rabbits is at risk because they can buckle when wet. Before the rabbits
can be rescued from Professor Boolean's lab, you must compute how much standing
water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and
water is poured from the top (and allowed to run off the sides). We'll assume
all the hutches are square, have side length 1, and for the purposes of this
problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3]:

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff,
it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os,
which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked
hutches from left-to-right as a list, computes the total area of standing water
accumulated as water is poured from the top and allowed to run off the sides.

The heights array will have at least 1 element and at most 9000 elements.
Each element will have a value of at least 1, and at most 100000.
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