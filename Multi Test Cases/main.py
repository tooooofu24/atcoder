T = int(input())
tests = []
for i in range(T * 2):
    if i % 2 == 0:
        input()
        continue
    numbers = list(map(int, input().split()))
    tests.append(numbers)


for numbers in tests:
    odd_count = 0
    for n in numbers:
        if n % 2 == 1:
            odd_count += 1
    print(odd_count)
