S = list(input())

KEYENCE = "keyence"

remove_count = len(S) - len(KEYENCE)

for i in range(8):
    s = S[:i] + S[i + remove_count :]
    if "".join(s) == KEYENCE:
        print("YES")
        exit()

print("NO")
