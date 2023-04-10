N, M = map(int, input().split())

l = []

for i in range(M * 2):
    if i % 2 == 0:
        input()
        continue
    l.append(list(map(int, input().split())))


booleans = [N in set(numbers) for numbers in l]

A = booleans.count(True)
B = booleans.count(False)

total = 0
for i in range(1, M + 1):
    total += (A + B) * (A + B - 1)(A + B - 2) / i - (B(B - 1)(B - 2) / i)

print(total)
