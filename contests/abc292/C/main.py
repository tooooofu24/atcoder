#!/usr/bin/env python3

N = int(input())

x = [0] * N

for i in range(1, N):
    for j in range(i, N, i):
        x[j] += 1
print(sum(x[i] * x[N - i] for i in range(1, N)))
