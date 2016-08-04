# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:57:45 2016

@author: Aaron Beckett
"""

import operator as op

def answer(seq):
    
    def nCk(n, k):
        k = min(k, n-k)
        if k == 0: return 1
        numer = reduce(op.mul, xrange(n, n-k, -1))
        denom = reduce(op.mul, xrange(1, k+1))
        return numer//denom
        
    def num_sequences(root):
        
        if root.size == 1:
            return 1
        
        left_seq = num_sequences(root.left) if root.left else 1
        right_seq = num_sequences(root.right) if root.right else 1
        
        m = root.left.size if root.left else 0
        n = root.right.size if root.right else 0
        
        return nCk(m+n, m) * left_seq * right_seq
        
    tree = BST()
    for n in seq:
        tree.insert(n)
        
    return num_sequences(tree.root)
        
        
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
