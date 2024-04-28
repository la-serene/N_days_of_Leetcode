# 392. Is sub seq
# Ez
# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).
"""


class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        """
            91.80% time, 89.13% mem
        """
        if len(s) == 0:
            return True

        i = 0
        for j in t:
            if j == s[i]:
                if i == len(s) - 1:
                    return True
                i += 1
