# 1791. Find Center of Star Graph
# Easy
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there
# is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the
# nodes ui and vi. Return the center of the given star graph.

class Solution:
    def findCenter(self, edges) -> int:
        d = {}
        for i in edges:
            a, b = i[0], i[1]
            if d.get(a, 0) == 0:
                d[a] = 1
            else:
                d[a] += b
            if d.get(b, 0) == 0:
                d[b] = 1
            else:
                d[b] += b
        return max(d, key=d.get)

