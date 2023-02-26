H, W = map(int, input().split())

grid = []
bomb_list = []
for i in range(H):
    y = i  # Y座標
    row = list(input())
    grid.append(row)
    # "#"が含まれるインデックスを取得
    x_list = [n for n, v in enumerate(row) if v == "#"]
    for x in x_list:
        bomb_list.append([y, x])

# 爆弾の周囲のマスを数える
