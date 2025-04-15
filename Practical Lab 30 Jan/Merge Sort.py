import time
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def measure_time_merge_sort(n):
    arr = np.random.randint(0, 1000, n).tolist()
    start = time.time()
    merge_sort(arr)
    end = time.time()
    return end - start

N_values = [10,250, 500, 1000, 5000, 10000, 25000, 50000,100000]
times_merge_sort = [measure_time_merge_sort(n) for n in N_values]


plt.plot(N_values, times_merge_sort, marker='o', linestyle='-', color='blue', label="Merge Sort (O(N log N))")
plt.xlabel("Input Size (N)")
plt.ylabel("Time Taken (seconds)")
plt.title("Merge Sort Time Complexity")
plt.legend()
plt.grid()
plt.show()
