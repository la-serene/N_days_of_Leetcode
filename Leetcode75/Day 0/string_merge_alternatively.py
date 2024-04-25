# 1768. Merge Strings Alternately
# Easy
# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        maxlen = max(len(word1), len(word2))

        for i in range(maxlen):
            if i < len(word1):
                result = result + word1[i]
            if i < len(word2):
                result = result + word2[i]

        return result
