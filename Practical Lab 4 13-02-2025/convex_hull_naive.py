def is_on_left(p1, p2, p):

    return (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []

    for i in range(n):
        for j in range(i + 1, n):
            a = points[i]
            b = points[j]

            left = right = False
            for k in range(n):
                if k == i or k == j:
                    continue
                position = is_on_left(a, b, points[k])
                if position > 0:
                    left = True
                elif position < 0:
                    right = True
            if not (left and right):
                if a not in hull:
                    hull.append(a)
                if b not in hull:
                    hull.append(b)


    cx = sum([p[0] for p in hull]) / len(hull)
    cy = sum([p[1] for p in hull]) / len(hull)
    hull.sort(key=lambda p: (math.atan2(p[1] - cy, p[0] - cx)))
    return hull


import math

points = [(0, 3), (2, 2), (1, 1), (2, 1),
          (3, 0), (0, 0), (3, 3)]

hull_points = convex_hull(points)
print("Convex Hull points (in counter-clockwise order):")
for p in hull_points:
    print(p)
