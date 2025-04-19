def find_2d_peak(matrix, rows, cols, mid_col):
    max_row = 0
    for i in range(rows):
        if matrix[i][mid_col] > matrix[max_row][mid_col]:
            max_row = i

    if (mid_col == 0 or matrix[max_row][mid_col] >= matrix[max_row][mid_col - 1]) and \
       (mid_col == cols - 1 or matrix[max_row][mid_col] >= matrix[max_row][mid_col + 1]):
        return matrix[max_row][mid_col]
    elif mid_col > 0 and matrix[max_row][mid_col] < matrix[max_row][mid_col - 1]:
        return find_2d_peak(matrix, rows, cols, mid_col - cols // 4)
    else:
        return find_2d_peak(matrix, rows, cols, mid_col + cols // 4)

matrix = [
    [10, 8, 10, 10],
    [14, 13, 12, 11],
    [15, 9, 11, 21],
    [16, 17, 19, 20]
]

rows = len(matrix)
cols = len(matrix[0])
peak = find_2d_peak(matrix, rows, cols, cols // 2)
print("One 2D peak element is:", peak)
