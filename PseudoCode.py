# = rules
## = pseudocode

# rules:
# rounds 1 and 2:

## create list of words to choose from (CSV file not necessary. text file accepltable)
## create list of wheel spaces to choose from (19 spots, not 24. 100-900 in $50 increments, plus lose a turn, plus bankrupt)
## create blanks (gameboard) list
## create letters guessed list
## create random mystery prize list (or, you can just do a flat ammount)

## create perm bank for player 1
## create perm bank for player 2
## create perm bank for player 3

## create random word generator using word list
    ## creates word to be guessed
    ## appends blanks (gameboard) list
## create random wheel space generator from list
## create random mystery prize generator from list

# puzzle of letters presented:
    ## call random word generator
    ## print display of word in blanks (gameboard)  list

# 3 players
# everyone starts with $0

## while loop:
    ## play below until someone solves the puzzle 
    # player 1 turn:
        # if player has money, choose to: 
            ## ask for user input regarding choice
                ## assign each choice a function/path
            ## create "bankEmpty" to check if bank has money or not
                ## if bank = 0:
                    ## spin
                    ## solve
                #if bank > 0:
                    ## spin
                    ## buy a vowel
                    ## solve 

            # 1) spin 
                ## call random wheel space generator
                    ## "spin" = result of function call above
                    ## if spin = prize:
                        ## ask for user input regarding letter choice
                        ## check to see if letter is in guessed letters list:
                            ## if yes:
                                ## guess again (repeat get input)
                            ## if no: 
                                ## check to see if letter is in puzzle:
                                    ## if yes:
                                        ## player bank + prize*[number of occurances of letter in word]
                                        ## append words guessed list
                                        ## append blanks (gameboard) list
                                        ## get input regarding whether player wnats to:
                                            ## spin
                                            ## buy a vowel
                                            ## solve
                                    ## if no: 
                                        ## append letters guessed list
                                        ## player's turn ends (move to next player)

            # 2) buy a vowel
                ## player bank - 250
                ## ask for user input regarding what vowel they would like to pick
                    ## check to see if letter is in puzzle:
                        ## if yes:
                            ## append words guessed list
                            ## append blanks (gameboard) list
                            ## get input regarding whether player wnats to:
                                ## spin
                                ## buy a vowel
                                ## solve
                        ## else: 
                            ## append letters guessed list
                            ## player's turn ends (move to next player)

            # 3) solve puzzle
                ## get user input regarding guess:
                    ## if guess == word:
                        ## round over!!!
                            ## players' banks for round stay intact
                            ## move onto round 2 or 3

        # else if player has NO money
            # solve (see above "code")
            # spin (see above "code")
                
    # player 2 repeats process
    # player 3 repeats process
    # round ends when someone solves the puzzle 
# ===========================================================================
# round 3:

# player picks a mystery prize
## call random mystery prize generator

# puzzle presented:
## call random word generator
## 

# default free letters given [r,s,t,l,n,e]
    # if letters above are in puzzle, they're shown in place
    ## append blanks (gameboard) list)

# player picks 3 more consonants and one more vowel
## get player input regarding choices
    # if letters above are in puzzle, they're shown in place
    ## append blanks (gameboard) list)

# player guesses puzzle (one chance)
## get player input regarding choice
## check to see if input (guess) == word
    # if right, player wins mystery prize
    # if incorrect, player does not win mystery prize

#=======================================================================================================================
# scratchpad
import random
f = open('EnglishWords.txt','rt')
wordDump = f.read()
wordList = wordDump.split()

## create list of wheel spaces to choose from (19 spots, not 24. 100-900 in $50 increments, plus lose a turn, plus bankrupt)
wheelSpaces = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, "Lose A Turn", "Bankruptcy"]
## create blanks (gameboard) list
gameboard = []
## create letters guessed list
guessedLetters = []

## create vowels list:
vowels = ["A","E","I","O","U"]


def wordGenerator():
    global word
    ## creates word to be guessed
    word = random.choice(wordList).upper()
    ## appends blanks (gameboard) list
    for letter in word:
        gameboard.append("_")
    ## prints gameboard
    print(gameboard)

# create random wheel space generator from list
def wheel():
    global spin
    spin = random.choice(wheelSpaces)
    if type(spin) == int:
        print(f"The wheel has landed on ${spin}!")
        chooseLetter() 
    elif spin == "Lose A Turn":
        print("Ohhhhh, I'm sorry... You've landed on 'Lose A Turn'.")
    elif spin == "Bankruptcy":
        print("Ooooooh, that stings... You've landed on 'Bankruptcy'...")
        tempBankX = [0] ###figure out how to designate banks...

def chooseTurn(): #### tested, function chooseTurn works
    print(f"These are the letters you've guessed: {guessedLetters}")
    print(f"This is the puzzle so far: {gameboard}")
    turnChoice = input("Okay! What would you like to do? Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [P]?:  ").upper()
    if turnChoice == "S":
        print("Okay, give the wheel a spin!!")
        wheel() #### NOT WORKING!!! #######################
        chooseLetter() ########### TEST!!! REMOVE LATER #############
        print("FLAG!!!!")
    elif turnChoice == "V":
        buyVowel() ## NEEDS TO BE MADE
    elif turnChoice == "P":
        solvePuzzle() ## NEEDS TO BE MADE
    else:
        print("Please pick either Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [P]")
        chooseTurn()

def chooseLetter(): ### TESTED chooseLetter function works
    letterChoice = input("What letter would you like to guess?: ").upper()
    if letterChoice in word and letterChoice not in vowels and letterChoice not in guessedLetters:
        guessedLetters.append(letterChoice)
        win = spin * word.count(letterChoice)
        print(win)
        print(f"These are the letters you've guessed: {guessedLetters}")
        print(f"This is the puzzle so far: {gameboard}")
        chooseTurn() ### TESTING ##############################################
    elif letterChoice in vowels:
        print("Excuse me, you have to pay for vowels! Please pick a consonant.")
        print(f"These are the letters you've guessed: {guessedLetters}")
        print(f"This is the puzzle so far: {gameboard}")
        chooseLetter()
    elif letterChoice in guessedLetters:
        print(f"{letterChoice} has already been guessed, please pick something else.")
        print(f"These are the letters you've guessed: {guessedLetters}")
        print(f"This is the puzzle so far: {gameboard}")
        chooseLetter()
    else:
        print(f"I'm sorry, {letterChoice} is not in the word.") ###### this needs testing
        guessedLetters.append(letterChoice)
        print(guessedLetters)

# wordGenerator()
wheel()
# print(word)
# print(spin)
def dumbfunction():
    print("I'm a dumb function")

# chooseTurn()
dumbfunction()


####### FUNCTION TO CHECK GUESS, WORD AND APPEND GAMEBOARD:
def checkAndAppend(puzzleWord,guess,correctGuesses):
    for place in range(len(x)):
        if puzzleWord[place] == guess:
            print(place)
            print(puzzleWord[place])
            correctGuesses[place] = guess

# for place in range(len(wordArray)):
#     if wordArray[place] == guess:
#         print(place)
#         print(wordArray[place])
#         correctGuesses[place] = guess

# print(wordArray)
# print(correctGuesses)

# print(wordArray)
# print(correctGuesses)
print(gameboard)
print(list(word))

