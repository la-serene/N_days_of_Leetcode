# 2678. Number of Senior Citizens
# Easy
# https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01

"""
You are given a 0-indexed array of strings details. Each element of details provides information about a given
passenger compressed into a string of length 15. The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.
"""

from typing import List


# Simple Solution
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        n = len(details)
        for i in range(n):
            if int(details[i][11:13]) > 60:
                count += 1
        return count


# Advanced Solution
class AdvancedSolution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        n = len(details)
        for i in range(n):
            if int(details[i][11]) * 10 + int(details[i][12]) > 60:
                count += 1
        return count
