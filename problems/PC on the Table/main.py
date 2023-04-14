H, W = map(int, input().split())

for _ in range(H):
    l = list(input())
    previous_string_is_T = False
    for index, s in enumerate(l):
        if s == "T":
            if previous_string_is_T:
                l[index - 1] = "P"
                l[index] = "C"
                previous_string_is_T = False
                continue
            else:
                previous_string_is_T = True
        else:
            previous_string_is_T = False
    print("".join(l))
