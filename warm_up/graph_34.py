# graphs
# DFS
# Топологическая сортировка
"""
Дан ориентированный граф. Необходимо построить топологическую сортировку.

Формат ввода
В первой строке входного файла два натуральных числа N и M (1 ≤ N, M ≤ 100 000) — количество вершин 
и рёбер в графе соответственно. Далее в M строках перечислены рёбра графа. Каждое ребро задаётся 
парой чисел — номерами начальной и конечной вершин соответственно.

Формат вывода
Выведите любую топологическую сортировку графа в виде последовательности номеров вершин 
(перестановка чисел от 1 до N). Если топологическую сортировку графа построить невозможно, выведите 
-1.
"""
from sys import setrecursionlimit

def dfs(graph: list, colors: list, now: int, path: list):
    """
    Depth first search
    """
    colors[now] = 1
    for neigh in graph[now]:
        if colors[neigh] == 0:
            dfs(graph, colors, neigh, path)
        elif colors[neigh] == 1:
            print(-1)
            exit(0)
    colors[now] = 2
    path.append(now)
    return

def main(N, M, ways):
    setrecursionlimit(100000)
    graph = [[] for _ in range(N+1)]
    for way in ways:
        graph[way[0]].append(way[1])
    colors = [0 for _ in range(N+1)]
    path = []
    for node in range(1, N+1):
        if colors[node] == 0:
            dfs(graph, colors, node, path)
    print(*path[::-1])


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    ways = []
    for _ in range(M):
        way = list(map(int, input().split()))
        ways.append(way)
    main(N, M, ways)
