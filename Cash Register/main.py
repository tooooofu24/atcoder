S = input()

# 何回連続で0が出てきたか
zero_count = 0

# 回答
answer = 0

for n in map(int, list(S)):
    if n == 0:
        zero_count += 1
        continue
    if zero_count > 0:
        double_zero_count = zero_count // 2
        single_zero_count = zero_count % 2
        answer += double_zero_count + single_zero_count
        zero_count = 0
    answer += 1

if zero_count > 0:
    double_zero_count = zero_count // 2
    single_zero_count = zero_count % 2
    answer += double_zero_count + single_zero_count

print(answer)
