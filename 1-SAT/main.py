N = int(input())

S = []
T = []

for _ in range(N):
    s = input()
    S.append(s)
    T.append(s.replace("!", ""))

S = set(S)
T = set(T)

for t in T:
    if t in S and ("!" + t) in S:
        print(t)
        exit()

print("satisfiable")
