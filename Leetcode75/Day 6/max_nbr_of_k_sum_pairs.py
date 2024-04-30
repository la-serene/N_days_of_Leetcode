# 1679. Max Number of K-Sum Pairs
# Medium
# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums.sort()
        res, l, r = 0, 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == k:
                res += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

        return res
