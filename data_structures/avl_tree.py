# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:58:54 2016

@author: Aaron Beckett
"""

class avl_tree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = self.Node(value)
        
        def insert_in_subtree(root, new_node):
            # If this subtree doesn't exist, we've found the correct location
            # for the new node. Return the new node as the root of this subtree
            if root is None:
                return new_node
                
            # Recursively insert into correct subtree
            if new_node.data <= root.data:
                root.left = insert_in_subtree(root.left, new_node)
            else:
                root.right = insert_in_subtree(root.right, new_node)
                
            # Rebalance this subtree
            bf = root.balance_factor()
            if bf >= 2:
                
    
    def delete(self, value):
        pass
        
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        node.left.parent = node
        new_root.right = node
        node.parent = new_root
        new_root.parent = None
        return new_root
    
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        node.right.parent = node
        new_root.left = node
        node.parent = new_root
        new_root.parent = None
        return new_root

    class Node:
        
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None
            self.height = 0
            
        def balance_factor(self):
            r = self.right.height if self.right else -1
            l = self.left.height if self.left else -1
            return r - l
            
        def update_height(self):
            r = self.right.height if self.right else -1
            l = self.left.height if self.left else -1
            self.height = max(r, l) + 1
            