# -*- coding: utf-8 -*-
"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead
of following the Fibonacci sequence like all good rabbits do, the zombit
population changes according to this bizarre formula, where R(n) is the number
of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one
zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor
Boolean's minions passed the time by playing a guessing game: when will the
zombit population be equal to a certain amount? Then, some clever minion
objected that this was too easy, and proposed a slightly different game: when
is the last time that the zombit population will be equal to a certain amount?
And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you
can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation
of an integer S, returns the largest n such that R(n) = S. Return the answer as
a string in base-10 representation. If there is no such n, return "None". S will
be a positive integer no greater than 10^25.

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"
"""

def answer(str_S):
    """
    R(0) = 1
    R(1) = 1
    R(2) = 2
    R(2n) = R(n) + R(n + 1) + n (for n > 1)
    R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

    This is a k-regualar sequence that has a very tricky and non-deterministic
    solution I can't do. Instead I'll perform two separate binary searches over
    even and odd values.
    
    Searching over even and odd values with two binary searches works becuase
    the even and odd parts of the sequence form two monotonically increasing
    sequences. Finding one case where an even time gives the correct population
    means you found the only even case. After doing the same for odd times,
    return the largest time between the odd and even times or None if that
    population was never found by the two searches and therefore isn't possible.
    """
    
    # Define memoized function to compute the population
    calculated = {0:1, 1:1, 2:2}
    def R(t):
        if t not in calculated:
            n = t / 2
            if t % 2 == 0: # even
                calculated[t] = R(n) + R(n+1) + n
            else: # odd
                calculated[t] = R(n-1) + R(n) + 1
        return calculated[t]
        
    P = int(str_S)  # Target population
    T = None        # Greatest time where population was P   
    
    # Binary search over even times between 0 and P
    left = 0
    right = P / 2
    a = right / 2
    while True:
        pop = R(2*a)
        if pop == P:
            T = 2*a
            break
        elif pop < P:
            left = a
        else:
            right = a
        if a == (left+right) / 2:
            break
        else:
            a = (left+right) / 2
    
    # Binary search over odd times between 0 and P
    left = 0
    right = P / 2
    b = right / 2 + 1
    while True:
        pop = R(2*b + 1)
        if pop == P:
            # Odd times yeild population S will always
            # be greater than their even counterparts
            # due to the nature of the sequence
            T = 2*b + 1
            break
        elif pop < P:
            left = b
        else:
            right = b
        if b == (left+right) / 2:
            break
        else:
            b = (left+right) / 2
    
    return T
    
    
