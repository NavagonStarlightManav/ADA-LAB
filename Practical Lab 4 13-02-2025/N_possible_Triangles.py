from itertools import combinations

def area(p1, p2, p3):
    return 0.5 * abs(
        p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])
    )

def all_possible_triangles(points):
    triangles = []
    for p1, p2, p3 in combinations(points, 3):
        if area(p1, p2, p3) != 0:
            triangles.append((p1, p2, p3))
    return triangles

# Example usage
points = [(0, 0), (1, 1), (2, 0), (1, -1)]
triangles = all_possible_triangles(points)

print("All possible non-degenerate triangles:")
for tri in triangles:
    print(tri)
