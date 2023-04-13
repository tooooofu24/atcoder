N, M = map(int, input().split())
members = []
for i in range(N):
    members.append(list(input()))

answer = 0
for i, member1 in enumerate(members):
    for member2 in members[i + 1 :]:
        hasInsoluble = False
        for m in range(M):
            if member1[m] == "o" or member2[m] == "o":
                continue
            else:
                hasInsoluble = True
                break
        if not hasInsoluble:
            answer += 1

print(answer)
