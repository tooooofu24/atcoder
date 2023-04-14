N = int(input())
S = list(input())
Q = int(input())

reversed = False

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if reversed:
            S[N - (A - 1)], S[N - (B - 1)] = (
                S[N - (B - 1)],
                S[N - (A - 1)],
            )
        else:
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
    else:
        reversed = not reversed

if reversed:
    S[N:], S[:N] = S[:N], S[N:]

print("".join(S))
