N, Q = map(int, input().split())

players = [0] * N

for _ in range(Q):
    c, x = map(int, input().split())
    index = x - 1
    if c == 1:
        # イエローカード
        players[index] += 1
    elif c == 2:
        # レッドカード
        players[index] += 2
    else:
        isLeft = players[index] >= 2
        print("Yes" if isLeft else "No")
