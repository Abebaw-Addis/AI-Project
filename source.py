word_grid = [
    ['-', '-', '1', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '*', '2', '*', '*', '*', '*', '6', '-'],
    ['-', '-', '*', '*', '-', '-', '-', '-', '-', '-'],
    ['-', '3', '*', '*', '*', '*', '*', '-', '-', '-'],
    ['-', '-', '*', '*', '-', '-', '5', '-', '-', '-'],
    ['-', '-', '*', '*', '-', '-', '*', '-', '-', '-'],
    ['-', '-', '*', '-', '-', '-', '*', '-', '-', '-'],
    ['-', '-', '*', '-', '-', '-', '*', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '*', '-', '-', '-'],
    ['*', '*', '*', '*', '*', '4', '-', '-', '-', '-'],
]

words_to_find = ["yohannes", "abnet", "daniel", "abebaw", "hanna", "kaleb"]
used_keys = []
for row in word_grid:
    print(" ".join(row))

clues = 5
score = 0
trial = 6
def printword(clues):
    for _ in range(trial):
        puzzleNumber = int(input("\nWrite the key number (1-6): "))
        if 1 <= puzzleNumber <= 6:
            wanthint = input("Do you want a clue? (y/n) ").lower()
            if wanthint == 'y':
                clues -= 1