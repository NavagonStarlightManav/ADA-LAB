INF = float('inf')


def multistage_graph_forward(Graph):
    n = len(Graph)


    fdist = [INF] * n
    fdist[0] = 0


    prev = [-1] * n


    for u in range(n):
        for v in range(u + 1, n):
            if Graph[u][v] != INF and Graph[u][v] != 0:
                if fdist[u] + Graph[u][v] < fdist[v]:
                    fdist[v] = fdist[u] + Graph[u][v]
                    prev[v] = u


    path = []
    current = n - 1
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return fdist[n - 1], path

Graph = [
    [INF, 1, 2, INF, INF, INF, INF, INF],
    [INF, INF, INF, 3, 4, INF, INF, INF],
    [INF, INF, INF, INF, INF, 5, 6, INF],
    [INF, INF, INF, INF, INF, INF, INF, 7],
    [INF, INF, INF, INF, INF, INF, INF, 8],
    [INF, INF, INF, INF, INF, INF, INF, 2],
    [INF, INF, INF, INF, INF, INF, INF, 3],
    [INF, INF, INF, INF, INF, INF, INF, INF]
]

cost, path = multistage_graph_forward(Graph)
print("Minimum cost from start to end:", cost)
print("Shortest path:", path)
