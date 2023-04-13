N = int(input())
strings = list(input())
length = len(strings)

for i in range(1, N):
    # i回分出力する
    answer = 0
    for j in range(N):
        # 最後の文字まで比較できたら出力してbreak
        if j + i == length:
            print(answer)
            break
        s1 = strings[j]
        s2 = strings[j + i]
        # s1とs2が異なるならanswerを+1して次の文字へ
        if s1 != s2:
            answer += 1
            continue
        # s1とs2が同じなら出力してbreak
        print(answer)
        break
