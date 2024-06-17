


import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        h = int(math.sqrt(c))
        for i in range(h, -1, -1):
            for j in range(i, -1, -1):
                # val = pow(i, 2) + pow(j, 2)
                # if val < c and (2 * pow(i, 2) < c):
                #     return False
                # elif val == c:
                #     return True
                print(f"{i} {j}")


s = Solution()
s.judgeSquareSum(4)
