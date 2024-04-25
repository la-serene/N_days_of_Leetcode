# 605. Can Place Flowers
# Easy
# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

# NOTE: There are 2 versions provided. Tha latter is more direct and faster solution.

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false
otherwise
"""

# This is first solution. Too long and many rules
class Solution1:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        len_bed = len(flowerbed)
        current_flower = sum(flowerbed)
        total_flower = current_flower + n
        min_bed_of_n = total_flower + total_flower - 1
        max_flower = int((len_bed + 1) / 2)

        if len_bed < min_bed_of_n:
            return False

        if max_flower - current_flower < n:
            return False

        if n == 0:
            return True

        if len_bed > 1:
            placed = 0
            for i in range(1, len_bed):
                if placed == n:
                    return True

                prev = flowerbed[i - 1]
                cur = flowerbed[i]

                if prev or cur:
                    continue

                if i == 1:
                    placed += 1
                    flowerbed[0] = 1
                    continue

                if i == (len_bed - 1):
                    placed += 1

                    return placed >= n

                if flowerbed[i + 1]:
                    continue
                else:
                    flowerbed[i] = 1
                    placed += 1

            return placed >= n

        if current_flower == 0:
            return n <= 1

        return n <= 0


# Improved version
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            n = n - 1 if flowerbed[0] == 0 else n
            return n <= 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            else:
                if flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
                    continue

                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1

        return n <= 0
