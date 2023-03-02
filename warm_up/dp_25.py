def main(coord):
    numbers = sorted(coord)
    dp_back = [numbers[1]-numbers[0]]
    dp_free = [numbers[1]-numbers[0]]
    for i in range(1, len(numbers)-2):
        new_len = numbers[i+1] - numbers[i]
        dp_back.append(dp_free[i-1] + new_len)
        dp_free.append(dp_back[i-1])
    ans = min(dp_back[-1], dp_free[-1])
    if len(numbers) > 2:
        ans += numbers[-1] - numbers[-2]
    print(ans)


if __name__ == "__main__":
    coord =  list(map(int, input().split()))
    main(coord)
