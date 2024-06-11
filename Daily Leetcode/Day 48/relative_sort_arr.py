# 1122. Relative Sort Array
# Ez
# https://leetcode.com/problems/relative-sort-array/description/

"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements
that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""


"""
Solution:
Using binary insert seems to yield slower result compared to simply looping to insert value.
"""

def binary_insert(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            # mid is always smaller than right
            if mid == right or target < arr[mid + 1]:
                return mid + 1
            else:
                left = mid + 1
        else:
            if arr[mid - 1] < target:
                return mid
            else:
                right = mid - 1

    return -1


class Solution:
    def relativeSortArray(self, arr1, arr2):
        d = {}
        outlier = [-1]

        for i, value in enumerate(arr2):
            d[value] = [value]

        for i, value in enumerate(arr1):
            lst_idx = d.get(value, [])
            if len(lst_idx) == 0:
                if len(outlier) != 1:
                    new_idx = binary_insert(outlier, value)
                    outlier.insert(new_idx, value)

                    # n_outlier = len(outlier)
                    # for j in range(n_outlier):
                    #     if value < outlier[j]:
                    #         outlier.insert(j, value)
                    #         break
                    #     else:
                    #         if j == (n_outlier - 1):
                    #             outlier.append(value)
                else:
                    outlier.append(value)
            else:
                lst_idx.append(value)

        res = []
        for key, value in d.items():
            res += d[key][:-1]

        res += outlier[1:]

        return res


s = Solution()
s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19, 100, 20, 40, 60, 80, 70, 22, 21, 15, 12, 16, 13], [2, 1, 4, 3, 9, 6])
