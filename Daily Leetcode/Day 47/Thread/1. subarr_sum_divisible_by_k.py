# 974. Subarray Sums Divisible by K
# Medium
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a
sum divisible by k.

A subarray is a contiguous part of an array.
"""

"""
Solution: Try Prefix Sum and Hashmap.

Instead of using current sum as key, I use remain of sum at each iteration.
Note that only increment a key's value after adding to count.
"""


class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        mp = {0: 1}
        cur_sum = 0
        count = 0

        for i in nums:
            cur_sum += i
            remain = cur_sum % k

            if not mp.get(remain, 0) == 0:
                count += mp[remain]
                mp[remain] += 1
            else:
                mp[remain] = 1

        return count
