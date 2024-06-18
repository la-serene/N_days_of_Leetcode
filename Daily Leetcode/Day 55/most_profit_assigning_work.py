# 826. Most Profit Assigning Work
# Medium
# https://leetcode.com/problems/most-profit-assigning-work/

"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most
worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker
cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.
"""


class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        m, n = len(worker), len(profit)
        projects = [(profit[i], difficulty[i]) for i in range(n)]
        projects = sorted(projects)[::-1]
        worker = sorted(worker)[::-1]

        max_profit, start = 0, 0
        for i in range(m):
            for j in range(start, n):
                if worker[i] >= projects[j][1]:
                    max_profit += projects[j][0]
                    start = j
                    break

        return max_profit


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]

s = Solution()
s.maxProfitAssignment(difficulty, profit, worker)
