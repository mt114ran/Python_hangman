def hangman(word):
    wrong = 0
    stages = ["",
              "_________      ",
              "|       |      ",
              "|       |      ",
              "|       o      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンゲームを始めます!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "予想する1文字を入力してください >>> "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose、正解は{}.".format(word))

hangman("kometomo")
