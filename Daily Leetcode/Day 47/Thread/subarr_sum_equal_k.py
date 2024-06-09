# 560. Subarray Sum Equals K
# Medium
# https://leetcode.com/problems/subarray-sum-equals-k/description/

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose
equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    @staticmethod
    def subarraySum(nums, k: int) -> int:
        mp = {0: 1}
        running_sum = 0
        count = 0
        for i in nums:
            running_sum += i
            count += mp.get(running_sum - k, 0)
            if mp.get(running_sum, 0) == 0:
                mp[running_sum] = 1
            else:
                mp[running_sum] += 1
        return count


arr = [1, 2, 3, 0, 6, 1, 2]
print(Solution.subarraySum(arr, 3))
