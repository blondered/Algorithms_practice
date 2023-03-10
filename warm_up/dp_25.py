# Dynamic programming

"""
В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется 
соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику была привязана хотя бы 
одна ниточка, а суммарная длина всех ниточек была минимальна.

Формат ввода
В первой строке входных данных записано число N — количество гвоздиков (2 ≤ N ≤ 100). В следующей 
строке заданы N чисел — координаты всех гвоздиков (неотрицательные целые числа, не превосходящие 
10000).

Формат вывода
Выведите единственное число — минимальную суммарную длину всех ниточек.
"""
def main(coord):
    numbers = sorted(coord)
    free = [0, numbers[1] - numbers[0]]
    back_done = [0, numbers[1] - numbers[0]]
    i = 2
    while i < len(numbers) - 1:
        back_done.append(free[i-1] + numbers[i] - numbers[i-1])
        free.append(min(back_done[i], back_done[i-1]))
        i += 1
    ans = free[i-1]
    if len(numbers) > 2:
        ans += numbers[i] - numbers[i-1]
    print(ans)


if __name__ == "__main__":
    n = int(input())
    coord = list(map(int, input().split()))
    main(coord)
