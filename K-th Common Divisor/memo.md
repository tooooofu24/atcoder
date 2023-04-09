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

range の使い方

```python
range(5)
> [0, 1, 2, 3, 4]

range(1, 5)
> [1, 2, 3, 4]

range(1, 5, 2)
> [1, 3]
```
