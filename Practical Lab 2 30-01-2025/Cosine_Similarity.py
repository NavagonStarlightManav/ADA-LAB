import time
import matplotlib.pyplot as plt
import math
import random


def generate_random_string(word_pool, size):
    return ' '.join(random.choices(word_pool, k=size))


def cosine_similarity(str1, str2):
    words1 = str1.lower().split()
    words2 = str2.lower().split()

    all_words = list(set(words1 + words2))

    freq1 = [words1.count(word) for word in all_words]
    freq2 = [words2.count(word) for word in all_words]

    dot = sum(f1 * f2 for f1, f2 in zip(freq1, freq2))
    mag1 = math.sqrt(sum(f ** 2 for f in freq1))
    mag2 = math.sqrt(sum(f ** 2 for f in freq2))

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot / (mag1 * mag2)


def measure_time_and_similarity(size, word_pool):
    str1 = generate_random_string(word_pool, size)
    str2 = generate_random_string(word_pool, size)

    start = time.time()
    similarity = cosine_similarity(str1, str2)
    end = time.time()

    return str1, str2, similarity, end - start


def main():
    word_pool = ["apple", "banana", "machine", "data", "science", "model", "code", "learn", "python", "java",
                 "sun", "moon", "star", "river", "forest", "car", "train", "sky", "cloud", "light",
                 "love", "music", "dream", "goal", "mind", "energy", "robot", "tech", "smart", "future"]


    demo_size = int(input(" Enter size for demo comparison ( 10): "))
    print("\n Generating two random strings of size", demo_size)
    demo_str1, demo_str2, demo_sim, demo_time = measure_time_and_similarity(demo_size, word_pool)
    print("\nString 1:", demo_str1)
    print("String 2:", demo_str2)
    print(f" Cosine Similarity: {demo_sim:.4f}")
    print(f"️ Time Taken: {demo_time:.6f} sec\n")


    sizes = list(map(int, input(" Enter input sizes for graph ( 50 100 300 500): ").split()))
    similarities = []
    times = []

    for size in sizes:
        _, _, sim, t = measure_time_and_similarity(size, word_pool)
        similarities.append(sim)
        times.append(t)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, similarities, marker='o', color='blue')
    plt.title("Cosine Similarity vs Input Size")
    plt.xlabel("Input Size (Words)")
    plt.ylabel("Cosine Similarity")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(sizes, times, marker='x', color='red')
    plt.title("Time Taken vs Input Size")
    plt.xlabel("Input Size (Words)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
