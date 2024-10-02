def plant_flower(lst, idx):
    for i in idx:
        lst[i] = 1


class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)
        if n < (m * k):
            return -1
        elif n == (m * k):
            return sorted(bloomDay)[-1]

        d = {}
        max_day = 1
        for i in range(n):
            max_day = max(max_day, bloomDay[i])
            if d.get(bloomDay[i], 0) == 0:
                d[bloomDay[i]] = [i]
            else:
                d[bloomDay[i]].append(i)

        planted = [0] * n
        for i in range(1, max_day + 1):
            bouquet_left = m
            if d.get(i, 0) != 0:
                plant_flower(planted, d[i])
                j = 0
                while j < n:
                    if sum(planted[j:j + k]) == k:
                        bouquet_left -= 1
                        j += k

                        if bouquet_left == 0:
                            return i
                        else:
                            continue

                    j += 1

        return -1


s = Solution()
# print(s.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
# print(s.minDays([1, 10, 3, 10, 2], 3, 1))
