# k = 2, N = 2
dp = [1, 1]


def sum_last_k(dp, k):
    ans = 0
    for i in range(1, k + 1):
        ans += dp[0 - i]
    return ans


def main(N, k):

    dp = [0]

    for i in range(k):
        ans = sum_last_k(dp, i) + 1
        dp.append(ans)

    if N <= k:
        print(dp[N-1])
    else:
        for i in range(N - k - 1):
            ans = sum_last_k(dp, k)
            dp.append(ans)
        print(dp[-1])


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    N, k = numbers
    main(N, k)
