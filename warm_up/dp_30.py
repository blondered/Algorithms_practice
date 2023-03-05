def main(N, first, M, second):
    dp = [[0] * (M+1)]
    for i in range(1, N+1):
        dp_line = [0]
        for j in range(1, M+1):
            prev = max(dp[i-1][j], dp_line[j-1])
            if first[i-1] == second[j-1]:
                dp_line.append(prev+1)
            else:
                dp_line.append(prev)
        dp.append(dp_line)
    print(dp)
    ans = []
    i = N
    j = M
    while dp[i][j] > 0:
        if max(dp[i-1][j], dp[i][j-1]) < dp[i][j]:
            ans.append(first[i-1])
        if dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(*ans[::-1])

            
    

if __name__ == "__main__":
    N = int(input())
    first = list(map(int, input().split()))
    M = int(input())
    second = list(map(int, input().split()))
    main(N, first, M, second)
