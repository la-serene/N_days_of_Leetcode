# 560. Subarray Sum Equals K
# Medium
# https://leetcode.com/problems/subarray-sum-equals-k/description/

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose
equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

"""
Solution: If the prefix sum up to ith index is X, and the prefix sum up to jth index is Y and
it is found that Y = X +k, then the required subarray is found with i as start index and j as end index.

More specifically, since in mp we save the previous sum, by taking current sum - k then check if (sum - k) 
present in mp, we know that in prev subarrs there are one or many subarr(s) that sums to (sum - k), so we will have
n valid subarr.

Like this:  [[] ... ] in which smaller [] sum to (sum - k) and large [] sum to sum, so large [] - small [] equal
to k.
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
