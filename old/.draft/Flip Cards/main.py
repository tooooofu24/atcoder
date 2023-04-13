N = int(input())

cards = []
for _ in range(N):
    A, B = input().split()
    cards.append([A, B])

previous_inside = "A"
previous_outside = "B"

three_same_count = 0
same_card_count = 0
both_reversible_count = 0
one_same_count = 0
all_different_count = 0

for card in cards:
    inside = card[0]
    outside = card[1]

    # 4つの数字全てが一致する場合、1通りも存在しないためその場で終了
    if previous_inside == inside == previous_outside == outside:
        print(0)
        exit()

    # 3つの数字が一致する場合
    elif (
        previous_inside == inside == previous_outside
        or previous_inside == inside == outside
        or previous_inside == previous_outside == outside
        or previous_outside == inside == outside
    ):
        three_same_count += 1

    # 2つのカードが同じカードだった場合
    elif (
        previous_inside == inside
        and previous_outside == outside
        or previous_inside == outside
        and previous_outside == inside
    ):
        same_card_count += 1

    # 両方両面同じ番号だった場合
    elif previous_inside == previous_outside and inside == outside:
        both_reversible_count += 1

    # 番号が一つ重複していた場合
    elif (
        previous_inside == inside
        or previous_inside == outside
        or previous_outside == inside
        or previous_outside == outside
    ):
        one_same_count += 1

    # 全て違う番号の場合
    elif (
        previous_inside != inside
        and previous_inside != outside
        and previous_outside != inside
        and previous_outside != outside
    ):
        all_different_count += 1

    else:
        print("error")

    previous_inside = inside
    previous_outside = outside

total = 2**N

# 全てのcountを出力する
print(
    three_same_count,
    same_card_count,
    both_reversible_count,
    one_same_count,
    all_different_count,
)

# 3つの数字が一致する場合
if three_same_count > 0:
    total -= (8 ** (N - 2)) * three_same_count

# 2つのカードが同じカードだった場合
if same_card_count > 0:
    total -= (4 ** (N - 2)) * same_card_count

# 両方両面同じ番号だった場合
# 何もしない

# 番号が一つ重複していた場合
if one_same_count > 0:
    total -= (2 ** (N - 2)) * one_same_count

# 全て違う番号の場合
# 何もしない

# 998244353で割る！
# total = total % 998244353

print(total)
