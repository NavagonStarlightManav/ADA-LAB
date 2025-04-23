def matrix_chain_order(dimensions):
    n = len(dimensions) - 1

    m = [[0] * n for _ in range(n)]

    # l is the chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n - 1]

# Example usage
dimensions = [10, 20, 30, 40, 30]
result = matrix_chain_order(dimensions)
print(f"Minimum number of multiplications is {result}")
