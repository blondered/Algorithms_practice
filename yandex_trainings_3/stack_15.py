# stack (LIFO)

"""
Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N 
городов, последовательно пронумерованных от 0 до N - 1 . Направление в сторону от первого города к 
нулевому названо западным, а в обратную — восточным.
Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое 
смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе.
Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами отправились на 
восток, покинув родные улицы, и двигались до тех пор, пока не приходили в город, в котором средняя 
цена проживания была меньше, чем в родном.

Формат ввода
В первой строке дано одно число N (2≤N≤105) — количество городов в Лайнландии. Во второй строке дано
 N чисел ai (0≤ai≤109) — средняя цена проживания в городах с нулевого по (N - 1)-ый соответственно.
Формат вывода
Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в который переселятся 
его изначальные жители. Если жители города не остановятся в каком-либо другом городе, отправившись в
 Восточное Бесконечное Ничто, выведите -1 .
"""

from sys import stdin


def main(N, cities):
    stack = []
    answer = [-1] * N
    for i, city in enumerate(cities):
        while stack and stack[-1][0] > city:
            answer[stack[-1][1]] = i
            stack.pop()
        stack.append((city, i))
    print(*answer, sep=" ")


if __name__ == "__main__":
    N = int(stdin.readline())
    cities = list(map(int, stdin.readline().split()))
    main(N, cities)
