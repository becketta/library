# -*- coding: utf-8 -*-
"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory,
you had to develop a system to track them, since some habitually continue to
gnaw on the heads of their brethren and need extra supervision.

For obvious reasons, you based your rabbit survivor tracking system on a binary
search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages and each,
luckily enough, had a distinct age.

For a given group, the first rabbit became the root,
and then the next one (taken in order of rescue) was added,
older ages to the left and younger to the right.

The order that the rabbits returned to you determined the end pattern of
the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation,
and you need to make sure that all of the modifications or pathogens
introduced by Professor Boolean are contained properly.

Since the tree did not preserve the order of rescue, it falls to you to figure
out how many different sequences of rabbits could have produced an identical
tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1],
it would result in a binary tree identical to one created from [5, 2, 9, 1, 8].

You must write a function answer(seq) that takes an array of up to 50 integers
and returns a string representing the number (in base-10) of sequences that
would result in the same tree as the given sequence.
"""

import operator as op

def answer(seq):
    
    def nCk(n, k):
        """Compute combinations of n choose k."""
        k = min(k, n-k)
        if k == 0: return 1
        numer = reduce(op.mul, xrange(n, n-k, -1))
        denom = reduce(op.mul, xrange(1, k+1))
        return numer / denom
        
    def num_sequences(root):
        """
        Return number of insert sequences that would make an equivalent tree.
        
        Args:
            root: Root node of a binary search tree.
        """
        if root.size == 1:
            return 1
        
        left_seq = num_sequences(root.left) if root.left else 1
        right_seq = num_sequences(root.right) if root.right else 1
        
        m = root.left.size if root.left else 0
        n = root.right.size if root.right else 0
        
        # For any set of sequences that could create the left and right BST
        # structure, the number of ways those two sequences can be interwoven
        # is the combination of n choose k, where n is the combined size of the
        # left and right subtree and k is the size of one of the subtrees. Then
        # the total possible sequences that yield the root tree is this number
        # times the number of possible sequences that form the left subtree times the
        # number of possible sequences that form the right subtree.
        return nCk(m+n, m) * left_seq * right_seq
        
    # Create binary search tree from sequence
    tree = BST()
    for n in seq:
        tree.insert(n)
    
    # Return number of sequences that would make an equivalent tree
    return num_sequences(tree.root)
        

# Implement a simple binary search tree only capable of inserting values    
class BST(object):
    
    root = None
    
    def insert(self, val):
        node = self.Node(val)
        if not self.root:
            self.root = node
        else:
            cur = self.root
            while True:
                cur.size += 1
                if val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = node
                        break
                elif val > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = node
                        break
    
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.size = 1
            self.right = None
            self.left = None
