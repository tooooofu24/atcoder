N = int(input())
A = map(int, input().split())

A = sorted(A, reverse=True)

result = 0

# 200で割った余りをリストに格納
l = [n % 200 for n in A]

# 重複を削除したもの
unique_l = set(l)

for i in unique_l:
    c = l.count(i)
    result += c * (c - 1) // 2

print(result)
