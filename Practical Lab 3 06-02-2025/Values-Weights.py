def knapsack_by_ratio(weights, values, capacity):
    n = len(weights)
    ratio_index = [(values[i] / weights[i], i) for i in range(n)]
    ratio_index.sort(reverse=True)  # Sort by value/weight ratio descending

    x = [0.0] * n
    U = capacity

    for ratio, i in ratio_index:
        if weights[i] <= U:
            x[i] = 1
            U -= weights[i]
        else:
            x[i] = U / weights[i]
            break
    return x

# Make sure inputs are defined
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Sorted by Value/Weight Ratio:")
print(knapsack_by_ratio(weights, values, capacity))
