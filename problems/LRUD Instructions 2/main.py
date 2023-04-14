N = int(input())
S = input()

# 操作
movements = list(S)

# 過去の座標
histories = ["0,0"]

# 現在の座標
current = "0,0"


for s in movements:
    current_x = int(current.split(",")[0])
    current_y = int(current.split(",")[1])
    if s == "L":
        position = str(current_x - 1) + "," + str(current_y)
    elif s == "R":
        position = str(current_x + 1) + "," + str(current_y)
    elif s == "U":
        position = str(current_x) + "," + str(current_y + 1)
    elif s == "D":
        position = str(current_x) + "," + str(current_y - 1)
    current = position
    histories.append(position)

if len(histories) != len(set(histories)):
    print("Yes")
else:
    print("No")
