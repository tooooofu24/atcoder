# Memo

入力

```python
N, M = map(int, input().split())
```

key, value で for を回す

```python
for index, item in enumerate(l):
    print(index, item)
```

for のワンライナー

```python
l = [n * 2 for n in numbers]
```

ソート

```python
# ミュータブル
l.sort()
# イミュータブル
sorted_l = sorted(l)
```
