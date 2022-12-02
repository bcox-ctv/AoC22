move = {"A": 0, "B": 1, "C":2, "X":0, "Y": 1, "Z":2}

comp = [
    [4, 8, 3],
    [1, 5, 9],
    [7, 2, 6]
]

comp2 = [
    [3, 4, 8],
    [1, 5, 9],
    [2, 6, 7]
]
file1 = open('full_input.txt')

score = 0

for line_no, line in enumerate(file1):
    key, value = line.split()
    print(f"{line_no} {move[key]} vs {move[value]}")
    score += comp2[move[key]][move[value]]
    print(score)