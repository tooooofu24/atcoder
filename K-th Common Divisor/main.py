A, B, K = map(int, input().split())

A_divisors = [i for i in range(1, A + 1) if A % i == 0]
B_divisors = [i for i in range(1, B + 1) if B % i == 0]

common_divisors = sorted(list(set(A_divisors) & set(B_divisors)), reverse=True)

print(common_divisors[K - 1])
