import random
import time
import matplotlib.pyplot as plt


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_time(N):
    arr = [random.randint(1, 10000) for _ in range(N)]
    start_time = time.time()
    quick_sort(arr)
    return time.time() - start_time


N_values = [int(x) for x in input("Enter values of N separated by spaces: ").split()]


times = []
for N in N_values:
    times.append(measure_time(N))

plt.plot(N_values, times, marker='o')
plt.title('Time Complexity of Quick Sort')
plt.xlabel('Input Size (N)')
plt.ylabel('Time (Seconds)')
plt.grid(True)
plt.show()
