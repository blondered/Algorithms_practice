# graphs
# Списки смежности
# DFS
# Компоненты связности в неориентированном графе
"""
Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту 
связности, содержащую первую вершину.

Формат ввода
В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и
 ребер в графе. В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, 
 которые соединяют ребра.

Формат вывода
В первую строку выходного файла выведите число K — количество вершин в компоненте связности. Во 
вторую строку выведите K целых чисел — вершины компоненты связности, перечисленные в порядке 
возрастания номеров.
"""

def dfs(graph: list, visited: list, now: int):
    """
    Depth first search
    """
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, visited, neigh)
    return

def main(N, M, ways):
    graph = [[] for _ in range(N+1)]
    for way in ways:
        graph[way[0]].append(way[1])
        graph[way[1]].append(way[0])
    visited = [False for _ in range(N+1)]
    dfs(graph, visited, 1)
    print(sum(visited))
    ans = [i for i in range(N+1) if visited[i]]
    print(*sorted(ans))


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    ways = []
    for _ in range(M):
        way = list(map(int, input().split()))
        ways.append(way)
    main(N, M, ways)
