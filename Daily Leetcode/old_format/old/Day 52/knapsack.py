n = 4
S = 6
w = [0, 2, 1, 4, 3]
v = [0, 3, 3, 4, 2]


def knapsack():
    dp = [[0] * 7 for _ in range(6)]

    for i in range(1, n + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= w[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])

    for i in range(n + 1):
        for j in range(S + 1):
            print(dp[i][j], end=" ")
        print()


if __name__ == "__main__":
    knapsack()
