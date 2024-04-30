# 643. Maximum Average Subarray I
# Ez
# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any
answer with a calculation error less than 10-5 will be accepted.
"""

arr = [0, 1, 1, 3, 3]


def findMaxAverage(nums, k: int) -> float:
    ans = -99999
    l, r = 0, 0
    sub_sum = 0

    while r < len(nums):
        sub_sum += nums[r]
        if r - l + 1 == k:
            if sub_sum / k > ans:
                ans = sub_sum / k
            sub_sum -= nums[l]
            l += 1
        r += 1

    return ans


findMaxAverage(arr, 4)
