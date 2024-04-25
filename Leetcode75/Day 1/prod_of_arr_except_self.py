# 238. Product of Array Except Self
# Medium
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        count_zero = 0
        lst_zero = []
        for i, value in enumerate(nums):
            if value != 0:
                prod *= value
            else:
                count_zero += 1
                lst_zero.append(i)

        if count_zero == 1:
            nums = [0] * len(nums)
            nums[lst_zero[0]] = prod
            return nums
        elif count_zero == 0:
            for i, value in enumerate(nums):
                nums[i] = int(prod / nums[i])
            return nums
        else:
            return [0] * len(nums)
