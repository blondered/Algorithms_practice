# Bin search
"""
Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер
 мечтает собрать наклейки со всеми встречающимися числами.

Диего собрал N наклеек, некоторые из которых, возможно, совпадают. Как-то раз к нему пришли K 
коллекционеров. i-й из них собрал все наклейки с номерами не меньшими, чем pi. Напишите программу, 
которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего. 
Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.

Формат ввода
В первой строке содержится единственное число N (0 ≤ N ≤ 100 000) — количество наклеек у Диего.

В следующей строке содержатся N целых неотрицательных чисел (не обязательно различных) — номера 
наклеек Диего. Все номера наклеек не превосходят 109.

В следующей строке содержится число K (0 ≤ K ≤ 100 000) — количество коллекционеров, пришедших к 
Диего. В следующей строке содержатся K целых чисел pi (0 ≤ pi ≤ 109), где pi — наименьший номер 
наклейки, не интересующий i-го коллекционера.

Формат вывода
Для каждого коллекционера в отдельной строке выведите количество различных чисел на наклейках, 
которые есть у Диего, но нет у этого коллекционера.
"""

from sys import stdin


def bin_search(numbers, limit):
    # number of elements less then the limit (return index of first element >= limit)
    # invariant:
    # l < limit
    # r >= limit
    right = len(numbers)
    left = -1
    while right - left > 1:
        search_ind = (right + left) // 2
        if numbers[search_ind] < limit:
            left = search_ind
        else:
            right = search_ind
    return right


def main(N, diego, K, interests):
    diego = sorted(list(set(diego)))
    answer = [0] * K
    for i, interest in enumerate(interests):
        answer[i] = bin_search(diego, interest)
    print(*answer, sep="\n")


if __name__ == "__main__":
    N = int(stdin.readline())
    diego = list(map(int, stdin.readline().split()))
    K = int(stdin.readline())
    interests = list(map(int, stdin.readline().split()))
    main(N, diego, K, interests)
