INF = float('inf')


def floyd_warshall(Graph):
    n = len(Graph)


    dist = [[Graph[i][j] for j in range(n)] for i in range(n)]


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist

Graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

shortest_paths = floyd_warshall(Graph)

print("All-Pairs Shortest Path Matrix:")
for row in shortest_paths:
    print(row)
