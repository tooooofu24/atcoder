import statistics

N = int(input())
points = list(map(int, input().split()))

sorted_points = sorted(points)
center_points = sorted_points[N : len(sorted_points) - N]

avg = statistics.mean(center_points)

print(avg)
