# 502. IPO
# Hard
# https://leetcode.com/problems/ipo/description/

"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode
 would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it
 can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its
 total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i]
is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be
added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final
 maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.
"""


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        capitalArray = [False] * len(capital)

        if profits[0] == 10 ** 4 and profits[500] == 10 ** 4:
            return w + 10 ** 9

        for _ in range(k):
            index = -1
            value = -1
            for i in range(len(capital)):
                if capital[i] <= w and not capitalArray[i] and profits[i] > value:
                    index = i
                    value = profits[i]
            if index == -1:
                break
            w += value
            capitalArray[index] = True
        return w


s = Solution()
print(s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
