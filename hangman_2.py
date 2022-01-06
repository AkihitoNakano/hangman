import random

def hangman(word):
    wrong = 0  # 間違えた数
    stages = ["",
              "_____________________ ",
              "                      ",
              "           |          ",
              "           0          ",
              "          /|\         ",
              "          / \         ",
              "                      "
              ]
    rletters = list(word)       # 一文字をリストに入れる
    board = ["_"] * len(word)   # 隠れた文字を_にして解答の文字の数だけ掛け合わせる
    win = False                 # 最初はまだ勝利していない状態
    print("ハングマンへようこそ")

    while wrong < len(stages) - 1:
        print("\n")
        msg = '一文字を予想してね: '
        char = input(msg)
        if len(char)>=2:
            print("一文字のみ入力してね")
            continue
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char    # boardの_をchar文字に入れ替え
            rletters[cind] = "$"  # 同じ文字が複数あった場合おかしくなるため正解したら＄に変える
        else:
            wrong += 1
        print("".join(board))     #AAA.join()はリストのオブジェクトをAAAで繋ぐメソッド
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print('あなたの勝ち')
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は{}".format(word))

if __name__ == "__main__":
    words = ["cat","avatar","tech","flog"]
    word = words[random.randint(0, len(words)-1)]
    hangman(word)
