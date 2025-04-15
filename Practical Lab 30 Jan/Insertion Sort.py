import time
import matplotlib.pyplot as plt
import numpy as np


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def measure_time(n):
    arr = np.random.randint(0, 1000, n).tolist()  # Generating random numbers
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    return end - start


def main():
    N_values = list(map(int, input("Enter values of N separated by space: ").split()))
    times = [measure_time(n) for n in N_values]

    plt.plot(N_values, times, marker='o', linestyle='-')
    plt.xlabel("Input Size (N)")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Insertion Sort Time Complexity")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
