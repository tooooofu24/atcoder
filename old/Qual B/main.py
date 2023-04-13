N, K = map(int, input().split())
participants = list(input())

# 残りの枠
remaining = K

# 回答
answer = ""

for participant in participants:
    # 残り枠が0の場合はxを追加
    if remaining == 0:
        answer += "x"
        continue
    # oの場合は残り枠を減らしてoを追加
    if participant == "o":
        remaining -= 1
        answer += "o"
        continue
    answer += "x"


print(answer)
