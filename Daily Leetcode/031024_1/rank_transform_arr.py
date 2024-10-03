# 1331. Rank Transform of an Array
# Easy
# https://leetcode.com/problems/rank-transform-of-an-array/description/

"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        copied_arr = arr.copy()
        copied_arr = sorted(copied_arr)
        d = {}
        r = 1

        for i in range(n):
            if d.get(copied_arr[i], -1) == -1:
                d[copied_arr[i]] = r
                r += 1

        for i in range(n):
            arr[i] = d[arr[i]]

        return arr
