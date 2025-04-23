INF = float('inf')


def multistage_graph(Graph):
    n = len(Graph)


    fdist = [INF] * n
    d = [-1] * n


    fdist[n - 1] = 0


    for j in range(n - 2, -1, -1):
        for r in range(j + 1, n):
            if Graph[j][r] != INF and Graph[j][r] != 0:
                if Graph[j][r] + fdist[r] < fdist[j]:
                    fdist[j] = Graph[j][r] + fdist[r]
                    d[j] = r


    path = [0]
    current = 0
    while d[current] != -1:
        path.append(d[current])
        current = d[current]

    return fdist[0], path

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

cost, path = multistage_graph(Graph)
print("Minimum cost from start to end:", cost)
print("Shortest path:", path)
