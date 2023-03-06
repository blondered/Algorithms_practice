

def main(N, prices):
    day_one = [50000 for _ in range(N+1)]
    if prices[0] > 100:
        day_one[1] = prices[0]
    else:
        day_one[0] = prices[0]
    dp = [day_one]
    for day in range(1, N):
        dp_line = []
        plus_one = []
        for num_coupons in range(N):
            if prices[day] > 100:
            




            if dp[-1][num_coupons + 1] <= dp[-1][num_coupons] + prices[day]:
                dp_line.append(dp[-1][num_coupons + 1])
            else:
                dp_line.append(dp[-1][num_coupons] + prices[day])
                if prices[day] > 100:
                    plus_one.append(num_coupons)
        if prices[day] > 100:
            dp_correct = [i for i in  dp_line]
            for correcting in plus_one:
                dp_correct[correcting + 1] = dp_line[correcting]
            dp_line = dp_correct

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
    for day in range(N-1, 0, -1):
        if dp[day][now_coupons] == dp[day-1][now_coupons + 1] and dp[day][now_coupons] != 50000:
            used_coupons += 1
            days_coupons.append(day+1)
            now_coupons += 1
        
    print(min_money)
    print(left_coupons, used_coupons)

    print(*sorted(days_coupons), sep="\n")


if __name__ == "__main__":
    N = int(input())
    prices = []
    for i in range(N):
        prices.append(int(input()))
    main(N, prices)
