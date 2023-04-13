l = []

# 入力
N, M = map(int, input().split())


# key, value で for を回す
for index, item in enumerate(l):
    print(index, item)


# for のワンライナー
l = [item * 2 for item in l]


# ソート
l.sort()
sorted_l = sorted(l)


# range の使い方
range(5)
# > [0, 1, 2, 3, 4]

range(1, 5)
# > [1, 2, 3, 4]

range(1, 5, 2)
# > [1, 3]


# 最大公約数
import math

math.gcd(12, 18)
# > 6


# 約数
N = 12
divisors = [i for i in range(1, N + 1) if N % i == 0]
# > [1, 2, 3, 4, 6, 12]


# 配列の集合を取得
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
commons = list(set(A) & set(B))
