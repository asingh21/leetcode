"""
Description: You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

# Difficulty: medium

# Data structure: disjoint sets - union
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0 or n is None:
            return 0

        self.root = [i for i in range(n)]
        self.count = n
        for node1, node2 in edges:
            self.union(node1, node2)

        return self.count

    def find(self, node):
        if node == self.root[node]:
            return node

        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        if root_node1 != root_node2:
            self.root[root_node2] = root_node1
            self.count -= 1

