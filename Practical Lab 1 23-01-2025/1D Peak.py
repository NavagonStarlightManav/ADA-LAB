def find_peak(arr, low, high):
    mid = (low + high) // 2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
       (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
        return arr[mid]
    elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
        return find_peak(arr, mid + 1, high)
    else:
        return find_peak(arr, low, mid - 1)

arr = [1, 3, 4, 5, 2, 7, 6]
peak = find_peak(arr, 0, len(arr) - 1)
print("One peak element is:", peak)
