N, K = map(int, input().split())
name_list = []
for i in range(N):
    name = input()
    name_list.append(name)

sorted_name_list = sorted(name_list[:K])

for name in sorted_name_list:
    print(name)
