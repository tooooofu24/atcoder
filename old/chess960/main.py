S = input()

first_B_index = S.find("B")
last_B_index = S.rfind("B")

if first_B_index % 2 == last_B_index % 2:
    print("No")
    exit()

first_R_index = S.find("R")
last_R_index = S.rfind("R")

K_index = S.find("K")

if first_R_index < K_index and K_index < last_R_index:
    print("Yes")
else:
    print("No")
