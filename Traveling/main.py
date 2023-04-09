N = int(input())
previous_t = 0
previous_x = 0
previous_y = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    t_is_even = t % 2 == 0
    x_plus_y_is_even = (x + y) % 2 == 0
    if not t_is_even and x_plus_y_is_even:
        print("No")
        exit()
    duration = t - previous_t
    x_diff = abs(x - previous_x)
    y_diff = abs(y - previous_y)
    if duration < x_diff + y_diff:
        print("No")
        exit()
    previous_t = t
    previous_x = x
    previous_y = y

print("Yes")
