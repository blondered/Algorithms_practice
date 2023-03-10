# dynamic programming (two parameters of different nature)
# prices and coupons within days
"""
Около Петиного университета недавно открылось новое кафе, в котором действует следующая система 
скидок: при каждой покупке более чем на 100 рублей покупатель получает купон, дающий право на один 
бесплатный обед (при покупке на сумму 100 рублей и меньше такой купон покупатель не получает).

Однажды Пете на глаза попался прейскурант на ближайшие N дней. Внимательно его изучив, он решил, что
 будет обедать в этом кафе все N дней, причем каждый день он будет покупать в кафе ровно один обед. 
 Однако стипендия у Пети небольшая, и поэтому он хочет по максимуму использовать предоставляемую 
 систему скидок так, чтобы его суммарные затраты были минимальны. Требуется найти минимально 
 возможную суммарную стоимость обедов и номера дней, в которые Пете следует воспользоваться 
 купонами.

Формат ввода
В первой строке входного файла записано целое число N (0 ≤ N ≤ 100). В каждой из последующих N строк
 записано одно целое число, обозначающее стоимость обеда в рублях на соответствующий день. Стоимость
   — неотрицательное целое число, не превосходящее 300.

Формат вывода
В первой строке выдайте минимальную возможную суммарную стоимость обедов. Во второй строке выдайте 
два числа K1 и K2 — количество купонов, которые останутся неиспользованными у Пети после этих N дней
 и количество использованных им купонов соответственно.

В последующих K2 строках выдайте в возрастающем порядке номера дней, когда Пете следует 
воспользоваться купонами. Если существует несколько решений с минимальной суммарной стоимостью, то 
выдайте то из них, в котором значение K1 максимально (на случай, если Петя когда-нибудь ещё решит 
заглянуть в это кафе). Если таких решений несколько, выведите любое из них.
"""


def main(N, prices):
    if N == 0:
        print(0)
        print(0, 0)
        exit(0)
    day_one = [50000 for _ in range(N + 1)]
    if prices[0] > 100:
        day_one[1] = prices[0]
    else:
        day_one[0] = prices[0]
    dp = [day_one]
    for day in range(1, N):
        dp_line = []
        for num_coupons in range(N):
            if prices[day] > 100 and num_coupons > 0:
                dp_line.append(
                    min(dp[-1][num_coupons + 1], dp[-1][num_coupons - 1] + prices[day])
                )
            elif prices[day] > 100 and num_coupons == 0:
                dp_line.append(dp[-1][num_coupons + 1])
            else:
                dp_line.append(
                    min(dp[-1][num_coupons + 1], dp[-1][num_coupons] + prices[day])
                )
        dp_line.append(50000)
        dp.append(dp_line)

    min_money = 50000
    left_coupons = 0
    for num_coupons, money in enumerate(dp[-1]):
        if money <= min_money:
            min_money = money
            left_coupons = num_coupons

    now_coupons = left_coupons
    used_coupons = 0
    days_coupons = []
    for day in range(N - 1, 0, -1):
        if (
            dp[day][now_coupons] == dp[day - 1][now_coupons + 1]
            and dp[day][now_coupons] != 50000
        ):
            used_coupons += 1
            days_coupons.append(day + 1)
            now_coupons += 1
        elif prices[day] > 100:
            now_coupons -= 1
    print(min_money)
    print(left_coupons, used_coupons)
    print(*sorted(days_coupons), sep="\n")


if __name__ == "__main__":
    N = int(input())
    prices = []
    for i in range(N):
        prices.append(int(input()))
    main(N, prices)
