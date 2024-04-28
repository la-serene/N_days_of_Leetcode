# 283. Move Zeroes
# Ez
# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

# NOTE: first solution is slow, but efficient in mem
#       REMEMBER that using 2 pointers is not same as 2 loop. the 2nd solution gives a view that we can use
#       an iterator variable for looping, then increase by 1 instead :V --> just O(n)

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    @staticmethod
    def moveZeroes1(nums) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

    @staticmethod
    def moveZeroes(nums) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums
