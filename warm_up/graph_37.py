# graphs
# Матрица смежности
# BFS
# Кратчайший путь в неориентированном графе
"""
В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Формат ввода
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица 
смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – 
начальной и конечной.

Формат вывода
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам 
путь. Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.

Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.
"""


def main(N, graph, A, B):
    queue = [A]
    head = 0
    steps = [-1 for _ in range(N)]
    steps[A] = 0
    while steps[B] == -1 and head < len(queue):
        prev = queue[head]
        for node, is_neigh in enumerate(graph[prev]):
            if is_neigh == 1 and steps[node] == -1:
                queue.append(node)
                steps[node] = steps[prev] + 1
        head += 1
    print(steps[B])

    if steps[B] > 0:
        ans = [B+1]
        path = steps[B]
        now = B
        while True:
            for node, is_neigh in enumerate(graph[now]):
                if is_neigh == 1 and steps[node] == path - 1:
                    ans.append(node+1)
                    now = node
                    path -= 1
                    if path == 0:
                        print(*ans[::-1])
                        exit(0)
        


if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph_line = list(map(int, input().split()))
        graph.append(graph_line)
    A, B = list(map(int, input().split()))
    main(N, graph, A-1, B-1)
