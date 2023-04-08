S = input()

strings = list(S)

alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

length = len(strings)
total = 0

for i in range(length):
    # 1のくらいから順番に足していく
    index = length - i - 1
    s = strings[index]
    n = alphabets.index(s) + 1
    total += n * (26**i)

print(total)
