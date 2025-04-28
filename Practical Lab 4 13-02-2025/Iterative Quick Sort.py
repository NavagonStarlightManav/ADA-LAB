def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def iterative_quick_sort(arr):
    stack = []
    stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


# Example usage
arr = [10, 7, 8, 9, 1, 5]
iterative_quick_sort(arr)
print("Sorted array is:", arr)
