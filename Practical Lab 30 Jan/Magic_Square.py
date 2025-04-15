import time
import matplotlib.pyplot as plt


def generate_magic_square(n):
    magic_square = [[0]*n for _ in range(n)]

    i, j = 0, n // 2
    num = 1

    while num <= n**2:
        magic_square[i][j] = num
        num += 1
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square


def display_square(square):
    for row in square:
        print(" ".join(f"{num:2}" for num in row))


def measure_time(n):
    start = time.time()
    _ = generate_magic_square(n)
    end = time.time()
    return end - start


def main():
    # Step 1: Show example magic square of size 5
    example_size = int(input("Enter magic square size for demo (must be odd): "))
    print(f"\n🔢 Magic Square of size {example_size}:\n")
    demo_square = generate_magic_square(example_size)
    display_square(demo_square)

    # Step 2: Input for measuring time on multiple sizes
    print("\nNow enter different odd sizes (space-separated) to measure time:")
    N_values = list(map(int, input().split()))

    times = []
    for n in N_values:
        t = measure_time(n)
        times.append(t)

    # Step 3: Plotting results
    plt.figure(figsize=(10, 4))

    # Time vs Size
    plt.subplot(1, 2, 1)
    plt.plot(N_values, times, marker='o', color='green')
    plt.xlabel("Magic Square Size (N)")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Time Complexity of Magic Square")
    plt.grid(True)

    # Visualization of Center Row (for fun!)
    plt.subplot(1, 2, 2)
    center_rows = [generate_magic_square(n)[n//2] for n in N_values]
    for i, row in enumerate(center_rows):
        plt.plot(row, label=f'N={N_values[i]}')
    plt.title("Middle Row Values of Magic Squares")
    plt.xlabel("Column Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
