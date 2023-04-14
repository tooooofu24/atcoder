N = int(input())

result = 0
for i in range(1, N + 1, 2):
    divisor_count = 0
    for j in range(1, N + 1):
        if i % j == 0:
            divisor_count += 1
    if divisor_count == 8:
        result += 1

print(result)
