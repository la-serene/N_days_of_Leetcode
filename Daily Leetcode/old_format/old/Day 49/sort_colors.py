# 75. Sort Colors
# Medium
# https://leetcode.com/problems/sort-colors/description/

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

"""
A kinda straight-forward solution.
"""

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        lst_1 = []
        lst_2 = []

        while i < n:
            if nums[i] == 1:
                lst_1.append(1)
                nums.pop(i)
                n -= 1
                continue
            elif nums[i] == 2:
                lst_2.append(2)
                nums.pop(i)
                n -= 1
                continue
            i += 1

        nums += lst_1
        nums += lst_2
        return nums
