# 974. Subarray Sums Divisible by K
# Medium
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a
sum divisible by k.

A subarray is a contiguous part of an array.
"""

arr = [4, 5, 0, -2, -3, 1]


def subarraysDivByK(nums, k: int) -> int:
    remainder = {}
    count = 0
    subarr_sum = 0

    for i in range(len(nums)):
        if nums[i] % k == 0:
            remainder[0] = i
            count += 1

    return count


print(subarraysDivByK(arr, 5))
