N, K = map(int, input().split())
foods = list(map(int, input().split()))

total = sum(foods)

c = 0

for i in range(total + 1):
    foods[i] = 0
