N, M = map(int, input().split())
problems = list(map(int, input().split()))
answers = list(map(int, input().split()))

total = 0
for answer in answers:
    index = answer - 1
    total += problems[index]

print(total)
