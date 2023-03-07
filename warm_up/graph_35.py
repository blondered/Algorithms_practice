# graphs
# Матрица смежности
# DFS
# Цикл в неориентированном графе
"""
Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его.

Формат ввода
В первой строке дано одно число n — количество вершин в графе ( 1 ≤ n ≤ 500 ). Далее в n строках 
задан сам граф матрицей смежности.

Формат вывода
Если в иcходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй 
строке выведите число k — количество вершин в цикле, а в третьей строке выведите k различных чисел —
 номера вершин, которые принадлежат циклу в порядке обхода (обход можно начинать с любой вершины 
 цикла). Если циклов несколько, то выведите любой.
"""

from sys import setrecursionlimit

def dfs(graph: list, colors: list, now: int, parent: int, ans: list):
    """
    Depth first search
    """
    colors[now] = 1
    for i in range(N):
        if graph[now][i] == 1 and parent != i:
            if colors[i] == 0:
                is_cycled = dfs(graph, colors, i, now, ans)
                if is_cycled:
                    if now == ans[0]:
                        print("YES")
                        print(len(ans))
                        print(*[node + 1 for node in ans])
                        exit(0)
                    ans.append(now)
                    return True
            elif colors[i] == 1:
                ans.append(i)
                ans.append(now)
                return True
    
    colors[now] = 2
    return False

def main(N, graph):
    setrecursionlimit(100000)
    colors = [0 for _ in range(N)]
    ans = []
    for node in range(N):
        if colors[node] == 0:
            dfs(graph, colors, node, -1, ans)
    print("NO")

if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph_line = list(map(int, input().split()))
        graph.append(graph_line)
    main(N, graph)
