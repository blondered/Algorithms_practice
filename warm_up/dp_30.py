# Dynamic programming (two parameters of same nature)
# Наибольшая общая подпоследовательность
"""
Даны две последовательности, требуется найти и вывести их наибольшую общую подпоследовательность.

Формат ввода
В первой строке входных данных содержится число N – длина первой последовательности (1 ≤ N ≤ 1000). 
Во второй строке заданы члены первой последовательности (через пробел) – целые числа, не 
превосходящие 10000 по модулю.

В третьей строке записано число M – длина второй последовательности (1 ≤ M ≤ 1000). В четвертой 
строке задаются члены второй последовательности (через пробел) – целые числа, не превосходящие 10000
 по модулю.

Формат вывода
Требуется вывести наибольшую общую подпоследовательность данных последовательностей, через пробел.
"""


def main(N, first, M, second):
    dp = [[0] * (M + 1)]
    for i in range(1, N + 1):
        dp_line = [0]
        for j in range(1, M + 1):
            prev = max(dp[i - 1][j], dp_line[j - 1])
            if first[i - 1] == second[j - 1]:
                prev = max(prev, dp[i - 1][j - 1] + 1)
            dp_line.append(prev)
        dp.append(dp_line)
    ans = []
    i = N
    j = M
    while dp[i][j] > 0:
        if first[i - 1] == second[j - 1] and dp[i - 1][j - 1] + 1 >= max(
            dp[i - 1][j], dp[i][j - 1]
        ):
            ans.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
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
