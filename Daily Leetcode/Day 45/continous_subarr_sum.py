# 523. Continuous Subarray Sum
# Medium
# https://leetcode.com/problems/continuous-subarray-sum

"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

"""
SOLUTION:

1st Brute-force: apparently not efficient.
2nd: try to minimize the computational burden by using a list to save the sum from 0 idx to ith idx, then perform minus
to get the sum instead of looping to calculate it. 87/99: Time limit with too long list.
3rd: use mod. Code below. Meh big brain:v
"""

arr = [25, 2, 4, 6, 7]


def checkSubarraySum(nums, k: int) -> bool:
    remainder_map = {0: -1}
    cumulative_sum = 0

    for i, num in enumerate(nums):
        cumulative_sum += num
        remainder = cumulative_sum % k
        if remainder in remainder_map:
            if i - remainder_map[remainder] > 1:
                return True
        else:
            remainder_map[remainder] = i
    return False


checkSubarraySum(arr, 6)
