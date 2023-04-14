N, T = map(int, input().split())
l = list(map(int, input().split()))

pre = 0
for i in l:
    if i == l[0]:
        pre = i
        continue
    diff = i - pre
    if diff <= T:
        print(i)
        exit()
    pre = i
print(-1)
