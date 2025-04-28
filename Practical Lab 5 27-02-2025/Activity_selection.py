import random

def activity_selection(start, finish):
    n = len(start)
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_end:
            selected.append(activities[i])
            last_end = activities[i][1]

    return selected


# Generate random activities
def generate_activities(n, max_time=100):
    start = [random.randint(0, max_time // 2) for _ in range(n)]
    finish = [s + random.randint(1, max_time // 2) for s in start]
    return start, finish


# Main driver
n = int(input("Enter number of activities to generate: "))
start_times, end_times = generate_activities(n)

print("\nGenerated Activities (start, finish):")
for s, f in zip(start_times, end_times):
    print(f"({s}, {f})")

selected = activity_selection(start_times, end_times)

print("\nSelected Activities (non-overlapping):")
for s, f in selected:
    print(f"({s}, {f})")
