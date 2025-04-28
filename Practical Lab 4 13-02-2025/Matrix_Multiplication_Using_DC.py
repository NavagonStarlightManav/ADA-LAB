import time
import random
import matplotlib.pyplot as plt


def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def divide_and_conquer_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = add_matrix(divide_and_conquer_multiply(A11, B11), divide_and_conquer_multiply(A12, B21))
    C12 = add_matrix(divide_and_conquer_multiply(A11, B12), divide_and_conquer_multiply(A12, B22))
    C21 = add_matrix(divide_and_conquer_multiply(A21, B11), divide_and_conquer_multiply(A22, B21))
    C22 = add_matrix(divide_and_conquer_multiply(A21, B12), divide_and_conquer_multiply(A22, B22))

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def generate_matrix(n):
    return [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]


# DEMO
print("Demo: Multiplying two 2x2 matrices using Divide and Conquer")
A_demo = generate_matrix(2)
B_demo = generate_matrix(2)

print("Matrix A:")
for row in A_demo:
    print(row)

print("\nMatrix B:")
for row in B_demo:
    print(row)

C_demo = divide_and_conquer_multiply(A_demo, B_demo)

print("\nResult Matrix C (A x B):")
for row in C_demo:
    print(row)

# User Input for Plotting
sizes = list(map(int, input("\nEnter list of matrix sizes (space-separated, power of 2): ").split()))

times = []

for size in sizes:
    A = generate_matrix(size)
    B = generate_matrix(size)

    start = time.time()
    divide_and_conquer_multiply(A, B)
    end = time.time()

    times.append(end - start)
    print(f"Size {size}x{size}: Time taken = {end - start:.6f} seconds")

# Plotting the graph
plt.plot(sizes, times, marker='o')
plt.title("Time Taken vs Matrix Size (Divide and Conquer Matrix Multiplication)")
plt.xlabel("Matrix Size (n x n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()
