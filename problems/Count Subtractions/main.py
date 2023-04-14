A, B = map(int, input().split())

result = 0


while True:
    if A == B:
        print(result)
        exit()
    elif A > B:
        diff = A - B
        divide_count = diff // B
        if divide_count == 0:
            A = A - B
        else:
            A = A - (B * divide_count)
    elif A < B:
        diff = B - A
        divide_count = diff // A
        if divide_count == 0:
            B = B - A
        else:
            B = B - (A * divide_count)
    # divide_countが0の場合は1にする
    if divide_count == 0:
        divide_count = 1
    result += divide_count
