"""
Description: You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

# Difficulty: medium

# Data structure: disjoint sets - union
"""

from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.root = [i for i in range(len(s))]
        self.rank = [1] * len(s)

        for node1, node2 in pairs:
            self.union(node1, node2)

        component_dict = {}
        for i in range(len(s)):
            root_node = self.find(i)
            if root_node not in component_dict:
                component_dict[root_node] = []
            component_dict[root_node].append(s[i])

        for key in component_dict:
            component_dict[key].sort(reverse=True)

        return_list = []
        for i in range(len(s)):
            root_node = self.find(i)
            return_list.append(component_dict[root_node].pop())
        return "".join(return_list)

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        if root_node1 != root_node2:
            if self.rank[node1] > self.rank[node2]:
                self.root[root_node2] = root_node1
            elif self.rank[node1] < self.rank[node2]:
                self.root[root_node1] = root_node2
            else:
                self.root[root_node2] = root_node1
                self.rank[root_node1] += 1
