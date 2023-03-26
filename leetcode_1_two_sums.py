"""
# Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# Difficulty: easy

# Data structure: dictionary
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or target is None:
            return []

        sum_dict = dict()
        for index in range(len(nums)):
            if nums[index] in sum_dict:
                return [sum_dict[nums[index]], index]
            else:
                sum_dict[target - nums[index]] = index
        return []