def knapsack_by_weight(weights, values, capacity):
    n = len(weights)
    weight_index = [(weights[i], i) for i in range(n)]
    weight_index.sort()  # Sort by weight ascending

    x = [0.0] * n
    U = capacity

    for wt, i in weight_index:
        if weights[i] <= U:
            x[i] = 1
            U -= weights[i]
        else:
            x[i] = U / weights[i]
            break
    return x

# Define inputs here before calling the function
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Sorted by Weight:")
print(knapsack_by_weight(weights, values, capacity))
