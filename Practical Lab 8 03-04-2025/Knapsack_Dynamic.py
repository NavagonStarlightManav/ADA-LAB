def knapsack(weights, values, W):
    n = len(weights)


    dp = [[0] * (W + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]


    selected_indices = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_indices.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    selected_indices.reverse()


    selected_items = [(idx, weights[idx], values[idx]) for idx in selected_indices]

    return dp[n][W], selected_items

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items_taken = knapsack(weights, values, capacity)

print("Maximum value:", max_value)
print("Items taken:")
for idx, w, v in items_taken:
    print(f" - Item {idx}: Weight = {w}, Value = {v}")
