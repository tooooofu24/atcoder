N, M = map(int, input().split())
numbers = []
tails = []

for i in range(N):
    numbers.append(input())

for i in range(M):
    tails.append(input())

answer = 0

for number in numbers:
    tail = number[3:]
    if tail in tails:
        answer += 1

print(answer)
