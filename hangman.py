def hangman(word):
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"] #store the hangman stages in a list
    remaining_letters = list(word) # store the word entered into a list called remaining letters
    letter_board = ["__"] * len(word) # create a list of blank spaces equal to the size of the entered list
    win = False #create a boolean called win and start it off equal to false
    print('Welcome to Hangman') # welcome the user to the game
    
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:                          #if your guess is in the list remaining_letters then:
            character_index = remaining_letters.index(guess)    #create a character_index variable and store the index of remaining_letters where your guess was found
            letter_board[character_index] = guess               #replace the blank space in letter_board with your guess
            remaining_letters[character_index] = '$'            #replace your guess in remaning_letters with a garbage character $
        else:
            wrong_guesses += 1                                  #if your guess i not in the list remaining_letters then increment wrong_guesses variable
        print((' '.join(letter_board)))                         #print the letter board with spaces separating each blank/found letter
        print('\n'.join(stages[0: wrong_guesses + 1]))          #print stages list separated by newline characters but only up to wrong_guesses + 1 index

        if '__' not in letter_board:                            #if there are no blanks in letter_board list
            print('You win! The word was:')                     #print that the user has won
            print(' '.join(letter_board))                       #print the letter board with all letters separated by spaces
            win = True                                          #change win variable to true and break from the while loop
            break
    if not win:                                                 #if win is not true and wrong_guesses >= len(stages)-1
        print('\n'.join(stages[0: wrong_guesses]))              #print stages list separated by newline characters up to wrong_guesses index
        print('You lose! The words was {}'.format(word))        #print that the user has lost

hangman("Stephen")
