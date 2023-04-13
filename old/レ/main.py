N, M = map(int, input().split())
numbers = list(map(int, input().split()))

answer = []
append_numbers = []

for i in range(1, N + 1):
    if i in numbers:
        append_numbers.append(i)
        continue
    # 末尾に追加
    answer.append(i)
    # append_numbersに値があれば、逆順にして末尾に追加する
    if len(append_numbers) > 0:
        append_numbers.reverse()
        answer.extend(append_numbers)
        append_numbers = []

print(" ".join(map(str, answer)))
