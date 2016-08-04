# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:54:23 2016

@author: Aaron Beckett
"""
import math

def floyd_warshall(adjacency_list):
    """
    Find shortest paths in a weighted graph with positive or negative edge weights.
    
    The algorithm assumes there are no negative cycles but can be used to detect
    negative cycles by checking for negative path lengths from a node back to
    itself in the dist matrix.
    
    Time complexity :
        Worst  : O(|V|^3)
        Best   : O(|V|^3)
        Average: O(|V|^3)
    Space complexity: O(|V|^2)
    """
    
    V = len(adjacency_list)
    
    #
    # Initialize VxV matricies that track minimum distance and path b/w verticies
    #
    dist = [[math.inf] * V for _ in range(V)]
    next_v = [[None] * V for _ in range(V)]
    
    # Distance from a node to itself is 0
    for i in range(V):
        dist[i][i] = 0
        
    # For each edge in the graph, set its weight in the distance matrix and
    # the destination in the path tracking matrix
    for origin,edges in enumerate(adjacency_list):
        for dest,weight in edges:
            dist[origin][dest] = weight
            next_v[origin][dest] = dest
            
    # Main Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_v[i][j] = next[i][k]
                    
def shortest_path(u, v, successors):
    if not successors[u][v]:
        return []
    path = [u]
    while u != v:
        u = successors[u][v]
        path.append(u)
    return path
