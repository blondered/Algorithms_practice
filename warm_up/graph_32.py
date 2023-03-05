# graphs
# DFS
# Компоненты связности
"""
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и 
вывести их.

Формат ввода
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках 
записаны по два числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.

Формат вывода
В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами 
компоненты связности в следующем формате: в первой строке количество вершин в компоненте, во второй 
- сами вершины в произвольном порядке.
"""
import sys

def dfs(graph: list, now: int, component: int, components: list):
    """
    Depth first search
    """
    components[now] = component
    for neigh in graph[now]:
        if components[neigh] == 0:
            dfs(graph, neigh, component, components)
    return

def main(N, M, ways):
    sys.setrecursionlimit(100000)
    graph = [[] for _ in range(N+1)]
    for way in ways:
        graph[way[0]].append(way[1])
        graph[way[1]].append(way[0])
    components = [0 for _ in range(N+1)]
    component = 1
    for node in range(1, N+1):
        if components[node] == 0:
            dfs(graph, node, component, components)
            component += 1
    print(component-1)
    ans = [[] for _ in range(component)]
    for node in range(1, N+1):
        ans[components[node]].append(node)
    for component in ans[1:]:
        print(len(component))
        print(*component)


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    ways = []
    for _ in range(M):
        way = list(map(int, input().split()))
        ways.append(way)
    main(N, M, ways)
