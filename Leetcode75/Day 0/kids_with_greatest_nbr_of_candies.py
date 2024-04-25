# 1431. Kids With the Greatest Number of Candies
# Easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of
candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        for idx in range(len(candies)):
            candies[idx] = (candies[idx] + extraCandies) >= maxCandies

        return candies
