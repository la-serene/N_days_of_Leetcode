# 2418. Sort the People
# Easy
# https://leetcode.com/problems/sort-the-people/description/?envType=daily-question&envId=2024-07-22

"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
"""

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        d = {}
        for i in range(n):
            d[heights[i]] = names[i]

        heights = sorted(heights, reverse=True)
        for i in range(n):
            names[i] = d[heights[i]]

        return names
