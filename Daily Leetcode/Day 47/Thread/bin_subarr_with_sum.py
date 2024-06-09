# 930. Binary Subarrays With Sum
# Medium
# https://leetcode.com/problems/binary-subarrays-with-sum/description/

"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Same as the Subarr sum equal K.
Sliding window is only applicable when we know for sure if the prefixsum is an increasing or decreasing function(i.e.
Monotonous in nature) like now, since there is no negative input. (LATER)

"""


class Solution:
    @staticmethod
    def numSubarraysWithSumByPrefixSumHashmap(nums, k: int) -> int:
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

    # @staticmethod
    # def numSubarraysWithSumUsingSlidingWindow(nums, goal: int) -> int:
    #
