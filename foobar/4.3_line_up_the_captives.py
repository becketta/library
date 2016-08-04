# -*- coding: utf-8 -*-
"""
Line up the captives
====================

As you ponder sneaky strategies for assisting with the great rabbit escape, you
realize that you have an opportunity to fool Professor Booleans guards into
thinking there are fewer rabbits total than there actually are.

By cleverly lining up the rabbits of different heights, you can obscure the
sudden departure of some of the captives.

Beta Rabbits statisticians have asked you for some numerical analysis of how
this could be done so that they can explore the best options.

Luckily, every rabbit has a slightly different height, and the guards are lazy
and few in number. Only one guard is stationed at each end of the rabbit line-up
as they survey their captive population. With a bit of misinformation added to
the facility roster, you can make the guards think there are different numbers
of rabbits in holding.

To help plan this caper you need to calculate how many ways the rabbits can be
lined up such that a viewer on one end sees x rabbits, and a viewer on the
other end sees y rabbits, because some taller rabbits block the view of the
shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm,
50 cm, 40 cm, and then 20 cm, a guard looking from the left side would see 2
rabbits (30 and 50 cm) while a guard looking from the right side would see 3
rabbits (20, 40 and 50 cm).

Write a method answer(x,y,n) which returns the number of possible ways to
arrange n rabbits of unique heights along an east to west line, so that only x
are visible from the west, and only y are visible from the east. The return
value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40.

The viewable rabbits from either side (x and y) will be as small as 1 and as
large as the total number of rabbits (n).

Test cases
==========

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Output:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Output:
    (string) "24"
"""

import operator
import functools
import math

def answer(x, y, N):
    """
    Calculate number of arrangements of N rabbits of unique heights in a straight
    line such that x are visible from the left and y are visible from the right.
    
    The concept here is to group the heights of the bunnies into subsets
    consisting of one rabbit, and all succeeding bunnies before the next
    visible rabbit. Excluding the tallest rabbit (n - 1), we'll have
    a total number of subsets equal to 'x + y - 2'. For example:
    
    Heights: 1,2,3,4, where x = 2 and y = 3 can be arranged as
    
        3,4,2,1 where the subsets are:
            --> [3],4,[2,1]
                [3],4,[2],[1] <--
                
        This shows that the number of subsets is equal to the number of
        bunnies that can be seen from that side (minus the tallest which can
        be seen from anywhere).
        
    Now that we know how many subsets there are, all we need to do is calculate
    how arrangements of rabbits will produce the desired number ofy subsets
    and multiply that by the number of ways we can arrange those subsets.
    
    Args:
        x: Number of rabbits visible from the left side.
        y: Number of rabbits visible from the right side.
        N: Total number of rabbits
        
    Returns:
        Number of ways to order N rabbits of different height such that x are
        visible from the left and y are visible from the right.
    """
    
    comb_cache = {}
    def nCk(n, k):
        """Compute number of ways to choose k elemens from n."""
        k = min(k, n-k)
        if k == 0:
            return 1
        elif k < 0:
            return 0
        elif (n,k) not in comb_cache:
            numer = functools.reduce(operator.mul, range(n, n-k, -1), 1)
            denom = math.factorial(k)
            comb_cache[n,k] = numer // denom
        
        return comb_cache[(n,k)]
       
    perm_cache = {}
    def arrange(n, k):
        """
        Calculate number of arrangements of n rabbits where k rabbits are visible from the front.
        
        Args:
            n: Total number of rabbits in the sequence.
            k: Number of rabbits visible from one side.
            
        Returns:
            Number of arrangements where k rabbits are visible from the front.
        """
        if k > n:
            # You can't see k rabbits if there are less than k rabbits.
            return 0
        elif k == n:
            # In order to see all the rabits they must be lined up from shortest to tallest.
            return 1
        elif k == 1:
            # The tallest rabbit must be in front and therefore the number of
            # arrangements is just the number of permutations of the remaining.
            return math.factorial(n-1)
        elif k == n-1:
            # There is only one pair of rabbits where the one in front hides
            # the one in back... return the number of ways to choose such a pair.
            return nCk(n, 2)
        elif (n,k) not in perm_cache:
            # New calculation, find answer then memoize.
            
            # Recursively find number of arrangements that have the shortest
            # element in front. By placing the shortest element in front, we
            # can consider one less rabbit and, since it's the shortest, it
            # will always be seen so we can require one fewer visible rabbit.
            shortest_in_front = arrange(n-1, k-1)
            
            # Recursively find number of arrangements that do not have the
            # shortest element in front. We can consider one fewer rabbit but,
            # since it was the shortest rabbit, it will always be hidden so
            # k will not change.
            shortest_not_in_front = arrange(n-1, k) * (n-1)
            
            perm_cache[(n,k)] = shortest_in_front + shortest_not_in_front
            
        return perm_cache[(n,k)]

    #
    # Calculate answer
    #

    # The number of subsets a solution will have. Remember a subset is at least
    # one rabbit followed by any number of shorter rabbits.
    num_subsets = x + y - 2
    
    # Find the number of ways to arrange the rabbits (minus the tallest), such
    # that there are num_subsets of rabbits.
    rabbit_arrangements = arrange(N-1, num_subsets)
    
    # Calculate the number of ways to arrange these subsets about the tallest
    # rabbit.
    subset_arrangements = nCk(num_subsets, x-1)
    
    # The final answer is the number of ways to make the correct number of
    # subsets times the number of ways to arrange the correct number of subsets.
    return rabbit_arrangements * subset_arrangements