# 10
# [5, 10, 20]

from sys import stdin


def bin_search(len_numbers, numbers, limit):
    right = len_numbers
    left = -1
    while right > left:
        search_ind = (right + left) // 2
        if numbers[search_ind] <= limit:
            if search_ind == len_numbers - 1:
                return len_numbers
            elif numbers[search_ind + 1] > limit:
                return search_ind + 1
            else:
                left = search_ind
                continue
        elif search_ind == 0:
            return 0
        else:
            right = search_ind
    return left


def main(N, diego, K, interests):
    diego = sorted(list(set(diego)))
    answer = [0] * K
    for i, interest in enumerate(interests):
        answer[i] = bin_search(N, diego, interest)
    print(*answer, sep="\n")


if __name__ == "__main__":
    N = int(stdin.readline())
    diego = list(map(int, stdin.readline().split()))
    K = int(stdin.readline())
    interests = list(map(int, stdin.readline().split()))
    main(N, diego, K, interests)
