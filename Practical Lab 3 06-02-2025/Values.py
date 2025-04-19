def knapsack_by_value(weights, values, capacity):
    n = len(weights)
    value_index = [(values[i], i) for i in range(n)]
    value_index.sort(reverse=True)  # Sort by values descending

    x = [0.0] * n
    U = capacity

    for val, i in value_index:
        if weights[i] <= U:
            x[i] = 1
            U -= weights[i]
        else:
            x[i] = U / weights[i]
            break
    return x

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Sorted by Value:")
print(knapsack_by_value(weights, values, capacity))
