import random


def hangman(word):
    wrong = 0
    stages = ["",
              "-------    ",
              "|     |    ",
              "|     o    ",
              "|    /|\   ",
              "|    / \   ",
              "|          "
              ]
    
    # "rletters" are list of word
    rletters = list(word)
    # "board" is showed display
    board = ["_"] * len(word)
    win = False
    print("Welcome to hang man")

    # Main loop
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Predicts one character")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        """
        Do "str.join(arr)" , we can get lile this code
        str ele0 str ele2 str ele3 ~
        """
        print(" ".join(board))
        print("/n".join(stages[1:wrong+1]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose")
        print("{}".format(word))


if __name__ == "__main__":
    word_list = ["cat", "dog", "pizza", "cake"]
    hangman(random.choice(word_list))
