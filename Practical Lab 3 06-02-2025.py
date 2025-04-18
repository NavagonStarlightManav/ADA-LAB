def fractional_knapsack(weights, values, capacity):
    n = len(weights)

    ratio = [(values[i] / weights[i], i) for i in range(n)]

    ratio.sort(reverse=True)

    x = [0.0] * n

    U = capacity

    for r, i in ratio:
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

solution = fractional_knapsack(weights, values, capacity)
print("Solution vector (fractions of items taken):", solution)
