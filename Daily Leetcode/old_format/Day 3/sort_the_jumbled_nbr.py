# 2191. Sort the Jumbled Numbers
# Medium
# https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24

"""
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system.
mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer
with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the
mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
"""

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_dict = {}
        mapped = []
        n = len(nums)
        for i in range(n):
            aftermap = 0
            value = nums[i]

            if value != 0:
                count = 0

                while value != 0:
                    res = value % 10
                    aftermap += mapping[res] * pow(10, count)
                    count += 1
                    value = int(value / 10)

                if not mapped_dict.get(aftermap, []):
                    mapped_dict[aftermap] = [nums[i]]
                else:
                    mapped_dict[aftermap].append(nums[i])

                mapped.append(aftermap)
            else:
                aftermap = mapping[0]

                if not mapped_dict.get(aftermap, []):
                    mapped_dict[aftermap] = [0]
                else:
                    mapped_dict[aftermap].append(0)

                mapped.append(aftermap)

        mapped = sorted(mapped)
        for i in range(n):
            value = mapped[i]
            mapped[i] = mapped_dict[value][0]
            mapped_dict[value].pop(0)

        return mapped
