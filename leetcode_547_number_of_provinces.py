"""
Description: here are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

# Difficulty: medium

# Data structure: disjoint sets - union
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
            return 0

        self.root = [i for i in range(len(isConnected))]
        self.rank = [1] * len(isConnected)
        self.count = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    self.union(i, j)
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
            if self.rank[root_node1] > self.rank[root_node2]:
                self.root[root_node2] = root_node1
            elif self.rank[root_node1] < self.rank[root_node2]:
                self.root[root_node2] = root_node1
            else:
                self.root[root_node2] = root_node1
                self.rank[root_node1] += 1
            self.count -= 1