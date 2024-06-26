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

clues = 4
score = 0
trial = 6
def printword(clues):
    for _ in range(trial):
        puzzleNumber = int(input("\nWrite the key number (1-6): "))
        if 1 <= puzzleNumber <= 6:
            wanthint = input("Do you want a clue? (y/n) ").lower()
            if wanthint == 'y':
                clues -= 1
                if clues >= 0:
                    cluefinder(puzzleNumber)
                    print(f"You have {clues} clues left")
                else:
                    print("You have used all the available clues")
                    theword = input("Write your guess word: ").lower()
                    wordcompare(puzzleNumber,theword)
            else:
                theword = input("Write your guess word: ").lower()
                wordcompare(puzzleNumber,theword)
        else:
            print("Invalid Input")
        print("\nROUND FINISHED!")                
    print(f"\nYou Played {trial} times \nScored: {score}")

def cluefinder(puzzleNumber):
    clues_dict = {
        1: "ከቡድኑ አባላት መካከል ስሙ ረጅም የሆነና በመካከሉ ሓን ያለው",
        2: "ከቡድኑ አባላት መካከል ስሙ ምሳሌ የሚል ትርጉም ይሰጣል",
        3: "ከቡድኑ አባላት መካከል ሁለቱ መካከለኛ ፊደሎች ሲነበቡ ኔ የሚል ቃል የሚሰጥ ስም",
        5: "ከቡድኑ አባላት መካከል ስሟ ባለ ሁለት ራባዓይ ቀለማት ናቸው",
    }
    print(f"Clue: {clues_dict.get(puzzleNumber, 'No clue available')}")

def wordcompare(puzzleNumber,theword):
    used_keys.append(puzzleNumber)
    if theword == words_to_find[puzzleNumber-1]:
        if used_keys.count(puzzleNumber) > 1:
            print("you have already used this")
        else:
            compute()
            print("You Won This Time!")
     else:
        print("You Loss This Time")


def compute():
    global score
    score+=1

printword(clues)

