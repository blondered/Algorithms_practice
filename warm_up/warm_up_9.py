# Prefix sum (2d)

"""
Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике
 с левым верхним углом (x1, y1) и правым нижним (x2, y2)

Формат ввода
В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов 
(1 ≤ K ≤ 100000). Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки 
матрицы (по модулю не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных 
пробелом x1 y1 x2 y2 — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 
1 ≤ y1 ≤ y2 ≤ M)

Формат вывода
Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов 
матрице в прямоугольнике (x1, y1), (x2, y2)
"""


def prefix_sum(N, M, matrix):
    ans = [[0 for j in range(M + 1)] for i in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            ans[i][j] = (
                ans[i - 1][j] + ans[i][j - 1] + matrix[i - 1][j - 1] - ans[i - 1][j - 1]
            )

    return ans


def query(prefixes, x_min, y_min, x_max, y_max):
    smallest = prefixes[x_min - 1][y_min - 1]
    biggest = prefixes[x_max][y_max]
    top = prefixes[x_min - 1][y_max]
    left = prefixes[x_max][y_min - 1]
    print(biggest - top - left + smallest)


if __name__ == "__main__":
    N, M, K = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        matrix_line = list(map(int, input().split()))
        matrix.append(matrix_line)
    prefixes = prefix_sum(N, M, matrix)
    for _ in range(K):
        x_min, y_min, x_max, y_max = list(map(int, input().split()))
        query(prefixes, x_min, y_min, x_max, y_max)
