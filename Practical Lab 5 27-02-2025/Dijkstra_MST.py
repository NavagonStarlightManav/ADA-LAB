import sys

V = 5  # You can change this based on your graph size

def min_distance(dist, spt_set):
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if not spt_set[v] and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v

    return min_index

def dijkstra(graph, src):
    dist = [sys.maxsize] * V
    dist[src] = 0
    spt_set = [False] * V

    for _ in range(V):
        u = min_distance(dist, spt_set)
        spt_set[u] = True

        for v in range(V):
            if (
                not spt_set[v]
                and graph[u][v] != 0
                and dist[u] + graph[u][v] < dist[v]
            ):
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)

def print_solution(dist):
    print("Vertex \tShortest Distance from Source")
    for i in range(V):
        print(f"{i} \t\t {dist[i]}")

# Example graph
graph = [
    [0, 10, 0, 0, 5],
    [0, 0, 1, 0, 2],
    [0, 0, 0, 4, 0],
    [7, 0, 6, 0, 0],
    [0, 3, 9, 2, 0]
]

dijkstra(graph, 0)
