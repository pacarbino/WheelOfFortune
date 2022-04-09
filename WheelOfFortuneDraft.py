# = rules
## = pseudocode

# rules:
# rounds 1 and 2:

## create list of words to choose from (CSV file not necessary. text file accepltable)
# from operator import countOf
import random
# from tkinter import E
f = open('EnglishWords.txt','rt')
wordDump = f.read()
wordList = wordDump.split()
########################################################################################################
## create list of wheel spaces to choose from (19 spots, $100-$900 in $50 increments, plus lose a turn, plus bankrupt)
wheelSpaces = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, "Lose A Turn", "Bankruptcy"]
## create blanks (gameboard) list
gameboard = []
## create letters guessed list
guessedLetters = []
## create vowels list:
vowels = ["A","E","I","O","U"]

########################################################################################################
# 3 players
# everyone starts with $0 ##### FUNCTIONS CAN READ BANKS, BUT CAN'T SEEM TO ADD/SUBTRACT TO/FROM THEM
## create perm and temp bank for player 1
permBank1 = 0
tempBank1 = 0
## create perm and temp bank for player 2
permBank2 = 0
tempBank2 = 0
## create perm and temp bank for player 3
permBank3 = 0
tempBank3 = 0

##### TEST TEMP BANK #############

tempBankX = 1000

########################################################################################################
## create board checker function:
def boardChecker(puzzleWord,guess,correctGuesses):  ### TESTED boardChecker function works
    for place in range(len(puzzleWord)):
        if puzzleWord[place] == guess:
            print(place) #TEST PRINT
            print(puzzleWord[place]) # TEST PRINT
            correctGuesses[place] = guess

########################################################################################################
## create random word generator using word list:
def wordGenerator(): ###TESTED wordGenerator function works
    global word
    ## creates word to be guessed
    word = random.choice(wordList).upper()
    ## appends blanks (gameboard) list
    for letter in word:
        gameboard.append("_")
    ## prints gameboard
    print(gameboard)

########################################################################################################
## create random wheel spin generator from list
def wheel():  ### TESTED, WORKING, EXCEPT for bank     #### FIX GLOBAL FUNCTIONS, ADD PARAMETERS INSTEAD!!!
    global tempBankX
    global spin
    spin = random.choice(wheelSpaces)
    if type(spin) == int:
        print(f"The wheel has landed on ${spin}!")
        chooseLetter() 
    elif spin == "Lose A Turn":
        print("Ohhhhh, I'm sorry... You've landed on 'Lose A Turn'.")
    elif spin == "Bankruptcy":
        print("Ooooooh, that stings... You've landed on 'Bankruptcy'...")
        tempBankX = 0 ###figure out how to designate banks... (I THINK I FIGURED IT OUT IN THEORY... )

########################################################################################################
## create buy a vowel function:
def buyVowel():
    global tempBankX
    if tempBankX >= 250:
        vowelChoice = input("Okay! What vowel would you like to buy?: ").upper()
        if vowelChoice in vowels and vowelChoice in word:
            tempBankX -= 250
            guessedLetters.append(vowelChoice)
            ##gameboard.append(vowelChoice) #### NEEDS TO BE SPECIFIED WHERE THIS IS A FILL IN FOR TESTING
            boardChecker(word,vowelChoice,gameboard)  ##TEST
            print(f"Good guess! {vowelChoice} is in the puzzle!")
            chooseTurn()
        elif vowelChoice in vowels and vowelChoice not in word:
            tempBankX -= 250
            guessedLetters.append(vowelChoice)
            print(f"Oooh, I'm sorry, {vowelChoice} is not in the puzzle...")
        elif vowelChoice not in vowels:
            print(f"Please pick a vowel! [A, E, I, O, U]")
            buyVowel()
        

########################################################################################################
# create choice of letter (consonant) function:
def chooseLetter(): ### TESTED chooseLetter function works
    global tempBankX
    print(f"This is the puzzle so far: {gameboard}")
    print(f"These are the letters you've guessed: {guessedLetters}")
    print(f"You have ${tempBankX} in the bank.")
    letterChoice = input("What letter would you like to guess?: ").upper()
    if letterChoice in word and letterChoice not in vowels and letterChoice not in guessedLetters:
        guessedLetters.append(letterChoice)
        boardChecker(word,letterChoice,gameboard)
        winnings = spin * word.count(letterChoice) 
        print(f"Good guess! {letterChoice} is in the puzzle!")
        print(f"You've just won ${winnings}!!!")
        tempBankX += winnings ###### SORT OF WORKING!!! ADDED GLOBAL TEMPBANKX TO BEGINNING OF FUNCTION
        chooseTurn() ### TESTING ##############################################
    elif letterChoice in vowels:
        print("Excuse me, you have to pay for vowels! Please pick a consonant.")
        chooseLetter()
    elif letterChoice in guessedLetters:
        print(f"{letterChoice} has already been guessed, please pick something else.")
        chooseLetter()
    else:
        print(f"I'm sorry, {letterChoice} is not in the puzzle...")
        guessedLetters.append(letterChoice)
        print(guessedLetters)

## create input prompts:
## choice of turn:
def chooseTurn(): #### tested, function chooseTurn works
    print(f"These are the letters you've guessed: {guessedLetters}")
    print(f"This is the puzzle so far: {gameboard}")
    print(f"You have ${tempBankX} in the bank.")
    turnChoice = input("Okay! What would you like to do? Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [P]?:  ").upper()
    if turnChoice == "S":
        wheel() #### NOT WORKING!!! #######################
    elif turnChoice == "V":
        buyVowel() ## NEEDS TO BE MADE
    elif turnChoice == "P":
        solvePuzzle() ## NEEDS TO BE MADE
    else:
        print("Please pick either Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [P]")
        chooseTurn()

## create function for spinWheel:  UNECESSARY???? JUST USE WHEEL???
# def spinWheel(): ######### NOT WORKING ########################
#     wheel()
#     if spin == int:
#         chooseLetter() 
#     elif spin == "Lose A Turn":
#         print("Ohhhhh, I'm sorry... You've landed on 'Lose A Turn'.")
#     elif spin == "Bankruptcy":
#         print("Ooooooh, that stings... You've landed on 'Bankruptcy'...")
#         tempBankX = [0] ###figure out how to designate banks...
######## TEST OF FUNCTIONS #####################
# wordGenerator()
# wheel()

# print(word)
# print(spin)

# chooseLetter()
print("***TEST FLAG***")
print("Welcome to Wheel of Fortune! Let's play a game!")
wordGenerator()
print(f"THE TEST WORD IS {word} ***TEST FLAG***")
chooseTurn()

################################################
# puzzle of letters presented:
## call random word generator &
## print display of word in blanks (gameboard) list
# wordGenerator()

## create conditions for while loop to operate
puzzleSolved = False

## while loop:
#while puzzleSolved == False:
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