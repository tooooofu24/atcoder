N = int(input())
strings = list(input())

answer = ""

# 直前がnかどうか
is_previous_n = False

for s in strings:
    # 直前がnかつ今回がaの場合
    if is_previous_n and (s == "a"):
        answer += "ya"
        is_previous_n = False
        continue
    # 今回がnの場合
    if s == "n":
        is_previous_n = True
    else:
        is_previous_n = False
    answer += s

print(answer)
