import math



def tsp(distances):
    n = len(distances)

    dp = [[math.inf] * n for _ in range(1 << n)]


    dp[1][0] = 0


    for mask in range(1, 1 << n):
        for u in range(n):
            if (mask >> u) & 1:
                prev_mask = mask ^ (1 << u)
                for v in range(n):
                    if (prev_mask >> v) & 1:
                        dp[mask][u] = min(dp[mask][u], dp[prev_mask][v] + distances[v][u])


    return min(dp[(1 << n) - 1][i] + distances[i][0] for i in range(1, n))



distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 10],
    [25, 30, 5, 10, 0]
]

result = tsp(distances)
print(f"Minimum cost for the Traveling Salesman Problem is {result}")
