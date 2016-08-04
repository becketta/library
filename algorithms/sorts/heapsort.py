# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:40:58 2016

@author: Aaron Beckett
"""

def heapsort(A):
    """
    Sorts A in ascending order using heapsort
    
    Heapsort is UNSTABLE, OFFLINE
    
    Time complexity :
        Worst  : O(N logN)
        Average: O(N logN)
        Best   : O(N logN)
    Space complexity: O(1) auxiliary
    """
    
    def swap(a, b):
        """Swap elements at indices a and b"""
        temp = A[a]
        A[a] = A[b]
        A[b] = temp
        
    def parent(i):
        """Returns parent index of position i"""
        return (i-1) // 2
    
    def left_child(i):
        """Returns index of left child of position i"""
        return 2*i + 1
    
    def right_child(i):
        """Returns index of right child of position i"""
        return 2*i + 2
        
    def maxheap_sift_down(start, end):
        """
        Repair the heap whose root element is at index 'start'
        
        Sift down assumes the heaps rooted at the children of start are valid.
        The function sift up can also be used when constructing a heap in place
        but the running time of sift down is O(N) while sift up is O(N logN).        
        """
        root = start
        
        # While the root has at least one child, check if it needs to be swapped
        while left_child(root) < end:
            left = left_child(root)
            right = left + 1
            mx_root = root
            
            # Determine the correct root
            if A[mx_root] < A[left]:
                mx_root = left
            if right < end and A[mx_root] < A[right]:
                mx_root = right
                
            # Swap the root with the correct root if needed
            if mx_root != root:
                swap(root, mx_root)
                root = mx_root    # Repeat to continue sift down on swapped child
            
    
    def max_heapify():
        """Puts elements of A in heap order in-place"""
        # Start is assigned the index in A of the last parent node
        start = parent(len(A)-1)
        
        # Progressively ensure A[start:N] is in heap order
        while start >= 0:
            # Sift down the node at start such that all node below start are in heap order
            maxheap_sift_down(start, len(A))
            start -= 1
    
    # Build binary heap
    max_heapify()
    
    # Construct sorted array by continuously moving largest element to the end
    #
    # Loop maintains the invariants that A[0:end+1] is a heap and everything beyond
    # end is greater than everything before (so A[end+1:] is in sorted order)
    end = len(A) - 1
    while end > 0:
        # A[0] is the largest element left in the heap
        swap(end, 0)
        # Sift whatever element got swapped with A[0] to its appropriate place in heap
        maxheap_sift_down(0, end)
        # Decrement size of heap because size of sorted portion has incremented
        end -= 1
    