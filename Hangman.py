import random

def hangman():
    word_list=["Hello","Python",'computer','fruit','apple']
    random_num=random.randint(0,4)
    word=word_list[random_num]
    wrong=0
    stage=["",
           "_________       ",           
           "|       |       ",
           "|       0       ",
           "|      /|\      ",
           "|      / \      ",
           "|"
           ]
    rletters=list(word)
    board=['__']*len(word)
    win=False
    print("Welcome to Hangman")
    while wrong<len(stage)-1:
        print('\n')
        guess=input("Guess a letter:")
        if guess in rletters:
            cind=rletters.index(guess)
            board[cind]=guess
            rletters[cind]='@'
        else:
            wrong+=1
        print(' '.join(board))
        print('\n'.join(stage[0:wrong+1]))
        if '__' not in board:
            print('You win!The word was:')
            print(' '.join(board))
            win=True
            break
    if not win:
        print('\n'.join(stage[0:wrong]))
        print('You lose!The word was {}.format(word)')
hangman()
        
    
