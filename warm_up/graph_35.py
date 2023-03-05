# graphs
# DFS
# Циклы
"""

"""

def dfs(graph: list, components: list, now: int, N: int, component: int, parent: int, hist: list):
    """
    Depth first search
    """
    hist.append(now+1)
    is_cycled = False
    components[now] = component
    neighbours = [node for node in range(N) if graph[now][node] == 1]
    for neigh in neighbours:
        if neigh == parent:
            continue
        if components[neigh] == -1:
            dfs(graph, components, neigh, N, component, now, hist)
        else:
            is_cycled = True
    return is_cycled

def main(N, graph):
    components = [-1 for _ in range(N)]
    component = 0
    for node in range(N):
        if components[node] == -1:
            history = []
            is_cycled = dfs(graph, components, node, N, component, -1, history)
            if is_cycled:
                print("YES")
                print(len(history))
                print(*history)
                # cycled_nodes = [i+1 for i in range(N) if components[i] == component]
                # print(len(cycled_nodes))
                # print(*cycled_nodes)
                return
        component += 1
    print("NO")

if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph_line = list(map(int, input().split()))
        graph.append(graph_line)
    main(N, graph)
