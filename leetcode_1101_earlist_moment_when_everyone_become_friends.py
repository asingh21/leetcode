"""
Description: There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

# Difficulty: medium

# Data structure: disjoint sets - union
"""

from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n == 0 or n is None:
            return -1

        self.root = [i for i in range(n)]
        self.count = n
        logs.sort(key=lambda x: x[0])
        for timestamp, node1, node2 in logs:
            self.union(node1, node2)
            if self.count == 1:
                return timestamp
        return -1

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

