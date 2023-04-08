N = int(input())
numbers = list(map(int, input().split()))
Q = int(input())
queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))


for query in queries:
    type = query[0]  # 1 or 2
    i = query[1] - 1
    if type == 1:
        x = query[2]
        numbers[i] = x
    elif type == 2:
        print(numbers[i])
