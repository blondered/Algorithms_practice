# dynamic programming
"""
По данному числу N определите количество последовательностей из нулей и единиц длины N, в которых 
никакие три единицы не стоят рядом.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 35.

Формат вывода
Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231-1.
"""


def main(number):
    if number == 1:
        print(2)
        return
    elif number == 2:
        print(4)
        return
    elif number == 3:
        print(7)
        return
    elif number == 4:
        print(13)
        return
    dp = [2, 4, 7, 13]
    for i in range(4, number):
        ans = dp[i - 1] * 2 - dp[i - 4]
        dp.append(ans)
    print(dp[-1])


if __name__ == "__main__":
    number = int(input())
    main(number)
