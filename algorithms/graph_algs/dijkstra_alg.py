# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:53:38 2016

@author: Aaron Beckett
"""

import math

def dijkstra(graph, A):
    """
    Find shortest path from A to all other nodes in graph with non-negative weights
    
    This is asymptotically the fastest known single-source shortest-path
    algorithm for arbitrary directed graphs with unbounded non-negative weights.
    
    See Uniform-Cost Search for infinite or very large graphs.
    
    Time complexity :
        Worst  : O(|E| + |V|log|V|)
    Space complexity: O(logN) auxiliary
    """
    
    # Initialization
    Q = []                  # Optimize by using priority queue instead of list
                            # Fibonacci heap would be best
    for v in graph.nodes:
        v.dist = math.inf   # Unknown distance from A to v
        v.prev = []         # Previous node in optimal path from A
        Q.append(v)         # All nodes initially in Q (unvisited nodes)
        
    A.dist = 0              # Distance from A to A
    
    while Q:
        u = min(Q, key=lambda n: n.dist)    # Source node will be selected first
        Q.remove(u)
        
        for v in u.neighbors:       # Each neighbor of u still in Q
            if v in Q:
                alt = u.dist + graph.length(u, v)
                if alt < v.dist:    # A shorter path has been found
                    v.dist = alt
                    v.prev = [u]
                elif alt == v.dist: # An equivalent path has been found
                    v.prev.append(u)
    
class Node:
    """A Node in a graph"""
    
    def __init__(self, neighbors): 
        self.neighbors = []
        
        self.dist = math.inf
        self.prev = []
        
class Graph:
    """A directed graph with non-negative weights"""
    
    def __init__(self, N):
        self.nodes = [Node() for _ in range(N)]
        self.edges = [[None] * N for _ in range(N)]
        
    def add_edge(self, A, B, weight = 1):
        """Add weighted edge from node A to B"""
        a = self.nodes.index(A)
        b = self.nodes.index(B)
        self.edges[a][b] = weight
        A.neighbors.append(B)
        
    def length(self, A, B):
        """Return length of edge from A to B if it exists"""
        a = self.nodes.index(A)
        b = self.nodes.index(B)
        return self.edges[a][b]