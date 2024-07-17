# 945. Minimum Increment to Make Array Unique
# Medium
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description

"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment
nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

"""
Solution: First, since order doesn't matter, we sort then loop from 1 to n to check if a candidate is equal or 
smaller than its precedent. If one of them satisfies, perform necessary action.

Res: 75.65% in time (623ms).
     93.91% in mem (30.00MB).
"""


class Solution:
    def minIncrementForUnique(self, nums) -> int:
        n = len(nums)
        count = 0

        if n != 1:
            nums = sorted(nums)
            for i in range(1, n):
                if nums[i] == nums[i - 1]:
                    count += 1
                    nums[i] += 1
                elif nums[i] < nums[i - 1]:
                    count += nums[i - 1] + 1 - nums[i]
                    nums[i] = nums[i - 1] + 1

        return count


s = Solution()
s.minIncrementForUnique([3, 2, 1, 2, 1, 7])
