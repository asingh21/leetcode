"""
Description: You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Difficulty: medium

# Data structure: disjoint sets - union
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        self.root = [i for i in range(n)]
        for node1, node2 in edges:
            if not self.union(node1, node2):
                return False
        print(f"set(self.root) = {set(self.root)}")
        print(f"self.root = {self.root}")
        return True

    def find(self, node):
        print(f"node = {node}, self.root = {self.root}")
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        if root_node1 == root_node2:
            return False
        self.root[root_node2] = root_node1
        return True
