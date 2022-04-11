# = rules
## = pseudocode

# rules:
# rounds 1 and 2:
def rules():
    print("""
    *******************************************************************************
    Welcome to Wheel of Fortune! 
    For those of you who have never played, 
    we're going to go over the rules of the game!
    
    A puzzle will be presented to you as a series of blanks an a gameboard.
    These blanks represent letters in a word that you have to guess.

    You have three choices of moves to make at the start of your turn:
        
        1) Spin the wheel! 
        
        If the wheel lands on a dollar amount,
        you can then try to guess one of the consonants in the word.

        If the letter you guess is in the word, the blanks on the gameboard
        will be replaced by the letter, and you will recieve the dollar amount 
        which your spin landed on multiplied times the number of times the 
        letter appears in the word. Your turn continues, and you are once again
        able to choose what you'd like to do next.
        
        If the letter is NOT in the word, you recieve no money for that spin. 
        Your turn is over, and the next player's turn begins.
        
        If the wheel lands on 'Lose A Turn', your turn immediately ends,
        and the next player's turn begins..
        
        If the wheel lands on 'Bankruptcy', you lose all the money in 
        your bank for that round, your turn ends, and the next player's turn begins..
        
        2) Buy a vowel! 
        
        If you have at least $250 in your current bank, you may choose
        to buy a vowel that you think might be in the puzzle.

        If you are right, the blanks in the gameboard are replaced by
        the vowel you've chosen, your turn continues, and you may once again
        choose which move you'd like to make next. 
        
        If you are wrong, your turn ends. 

        Either way, $250 is deducted from your bank for that round.
        
        3) Solve the puzzle!
        
        If you think you know what the word is, you may choose to 
        solve the puzzle. You guess a word, and if you are right, the
        puzzle is solved and all the money you've won from that round
        is transfered to your permanent bank.
        
        If you guess incorrectly, your turn ends, and the next player's turn begins.
        
    This cycle continues moving from player 1 to 2 to 3 and then back to plyer 1 until
    the puzzle is solved. After 2 rounds, the player with the most money in their
    permanent bank goes on to the bonus round 3.

    In round 3, the player is once again presented with a puzzle on gameboard.
    however, in this round, there is no spinning the wheel. Instead, 
    the default letters 'R, S, T, L, N, E' will be checked against the 
    puzzle and the gameboard will change to show where any of those letters
    are if they are in the puzzle.

    Next the player will select 3 more consonants and 1 more vowel.
    These letters will then be checked against the puzzle and revealed
    in the same manner as the letters above. 

    Player will then have 1 guess to try and solve the puzzle.

    If they guess correctly, they win the bonus prize of $25,000
    on top of all the money they won from the previous rounds.

    If they guess incorrectly, they still get to keep the money from the previous rounds,
    however they will not get the additional $25,000 prize.

    So, who's ready to play...

    Wheel!  Of!  Fortune!!!!!
    *******************************************************************************
    """)

########################################################################################################
## create list of words to choose from
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
## create words guessed list:
guessedWords = []
## create vowels list:
vowels = ["A","E","I","O","U"]


########################################################################################################
# 3 players
# everyone starts with $0 ##### FUNCTIONS CAN READ BANKS, BUT CAN'T SEEM TO ADD/SUBTRACT TO/FROM THEM
## create perm and temp bank for player 1
player1 = "Player 1"
permBank1 = 11
tempBank1 = 1  #### TEST, FIX LATER
## create perm and temp bank for player 2
player2 = "Player 2"
permBank2 = 22
tempBank2 = 2
## create perm and temp bank for player 3
player3 = "Player 3"
permBank3 = 33
tempBank3 = 3

##### TEST TEMP AND PERM BANK #############

# tempBankX = 1000
# permBankX = 0

########################################################################################################
## create board checker function:
def boardChecker(puzzleWord,guess,correctGuesses):  ### TESTED boardChecker function works
    for place in range(len(puzzleWord)):
        if puzzleWord[place] == guess:
            # print(place) #TEST PRINT
            # print(puzzleWord[place]) # TEST PRINT
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
## create random wheel spin generator from list:
def wheel(playerX, tempBankX, permBankX, puzzleSolved):  ### TESTED, WORKING, EXCEPT for bank     #### FIX GLOBAL FUNCTIONS, ADD PARAMETERS INSTEAD?!!!
    global spin
    # puzzleSolved
    spin = random.choice(wheelSpaces)
    if type(spin) == int:
        print(f"The wheel has landed on ${spin}!")
        chooseLetter(playerX, tempBankX, permBankX, puzzleSolved) 
    elif spin == "Lose A Turn":
        print(f"Ohhhhh, {playerX}, I'm sorry... You've landed on 'Lose A Turn'. Your turn is over.")
    elif spin == "Bankruptcy":
        print(f"Ooooooh, {playerX} that stings... You've landed on 'Bankruptcy'... ")
        tempBankX = 0 ###figure out how to designate banks... (I THINK I FIGURED IT OUT IN THEORY... )


########################################################################################################
## create solve function:
def solvePuzzle(playerX, tempBankX, permBankX, puzzleSolved):
    puzzleSolved
    playerX
    # global puzzleSolved
    global word
    # global solution
    solution = input("Okay, what do you think the answer to the puzzle is?: ").upper()
    if solution == word:
        print(f"YES! You did it! The answer was {word}!! Congratulations, you've won the round!!")
        print(f"You've just won a total of ${tempBankX}!!!")
        permBankX += tempBankX
        print(f"You now have a total of ${permBankX} in your permanent bank!")
        puzzleSolved = True  ##### doesn't seem to be making puzzleSolved true... seems to work in chooseLetter and buyVowel...
        print(solution)#### TEST PRINT!!
        print(word) ### TEST PRINT!!!
    elif solution != word:
        print(f"Unfortunately, no, {solution} is not the answer.")
        guessedWords.append(solution)


########################################################################################################
## create buy a vowel function:
def buyVowel(playerX, tempBankX, permBankX, puzzleSolved):
    # puzzleSolved
    if tempBankX >= 250:
        vowelChoice = input("Okay! What vowel would you like to buy?: ").upper()
        if vowelChoice in vowels and vowelChoice in word:
            tempBankX -= 250
            guessedLetters.append(vowelChoice)
            boardChecker(word,vowelChoice,gameboard)  ##TEST
            print(f"Good guess! {vowelChoice} is in the puzzle!")
            if gameboard == list(word):
                print(f"YES! You did it! The answer was {word}!! Congratulations, you've won the round!!")
                print(f"You've just won a total of ${tempBankX}!!!")
                permBankX += tempBankX
                print(f"You now have a total of ${permBankX} in your permanent bank!")
                puzzleSolved = True
            elif gameboard != list(word):
                chooseTurn(playerX, tempBankX, permBankX, puzzleSolved)
        elif vowelChoice in vowels and vowelChoice not in word:
            tempBankX -= 250
            guessedLetters.append(vowelChoice)
            print(f"Oooh, I'm sorry, {playerX}, {vowelChoice} is not in the puzzle...")
        elif vowelChoice not in vowels:
            print(f"Please pick a vowel! [A, E, I, O, U]")
            buyVowel(playerX, tempBankX, permBankX)
    elif tempBankX < 250:
        print("I'm sorry, {playerX}you must have at least $250 to buy a vowel. Please pick eitherSpin the Wheel [S], or Solve the Puzzle [SOLVE]")
        chooseTurn(playerX, tempBankX, permBankX)
        

########################################################################################################
# create choice of letter (consonant) function:
def chooseLetter(playerX, tempBankX, permBankX, puzzleSolved): ### TESTED chooseLetter function works
    # playerX
    # tempBankX 
    # permBankX
    # puzzleSolved
    letterChoice = input("What letter would you like to guess?: ").upper()
    if letterChoice in word and letterChoice not in vowels and letterChoice not in guessedLetters:
        guessedLetters.append(letterChoice)
        boardChecker(word,letterChoice,gameboard)
        winnings = spin * word.count(letterChoice) 
        print(f"Good guess! {letterChoice} is in the puzzle!")
        print(f"You've just won ${winnings}!!!")
        tempBankX += winnings ###### SORT OF WORKING!!! ADDED GLOBAL TEMPBANKX TO BEGINNING OF FUNCTION
        if gameboard == list(word):
            print(f"YES! You did it, {playerX}! The answer was {word}!! Congratulations, you've won the round!!")
            print(f"You've just won a total of ${tempBankX}!!!")
            permBankX += tempBankX
            print(f"You now have a total of ${permBankX} in your permanent bank!")
            puzzleSolved = True
        elif gameboard != list(word):
            chooseTurn(playerX, tempBankX, permBankX, puzzleSolved)
    elif letterChoice in vowels:
        print("Excuse me, you have to pay for vowels! Please pick a consonant.")
        chooseLetter(playerX, tempBankX, permBankX, puzzleSolved)
    elif letterChoice in guessedLetters:
        print(f"{letterChoice} has already been guessed, please pick something else.")
        chooseLetter(playerX, tempBankX, permBankX, puzzleSolved)
    else:
        print(f"I'm sorry, {letterChoice} is not in the puzzle...")
        guessedLetters.append(letterChoice)
        print(guessedLetters)

########################################################################################################
## create input prompts:
## choice of turn:
def chooseTurn(playerX, tempBankX, permBankX, puzzleSolved): #### tested, function chooseTurn works
    puzzleSolved
    print(f"{playerX}, it is your turn!")
    print(f"These are the letters that have been guessed: {guessedLetters}")
    print(f"This is the gameboard so far: {gameboard}")
    print(f"You have ${tempBankX} in the bank.")
    turnChoice = input(f"Okay, {playerX}, What would you like to do? Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [SOLVE]?:  ").upper()
    if turnChoice == "S":
        wheel(playerX, tempBankX, permBankX, puzzleSolved) 
    elif turnChoice == "V":
        buyVowel(playerX, tempBankX, permBankX, puzzleSolved) 
    elif turnChoice == "SOLVE":
        solvePuzzle(playerX, tempBankX, permBankX, puzzleSolved)
    else:
        print("Please pick either Spin the Wheel [S], Buy a Vowel [V], or Solve the Puzzle [SOLVE]")
        chooseTurn(playerX, tempBankX, permBankX, puzzleSolved)

########################################################################################################

## Begin Game!
## create conditions for while loop to operate
puzzleSolved = False
roundCounter = 1 
rules()
##wordGenerator()
##print(word) ###TEST

while roundCounter <= 2:
    puzzleSolved
    print(f"Okay, Players! This is round {roundCounter}!")
    wordGenerator()
    print(f"Your puzzle is: {gameboard}")
    print(word) ###TEST


    while puzzleSolved == False:

        chooseTurn(player1, tempBank1, permBank1, puzzleSolved)  ##create player parameter for "playerX"
        print(f"permbank: {permBank1}")  ### TEST!!!
        print(f"tempbank: {tempBank1}")

        chooseTurn(player2, tempBank2, permBank2, puzzleSolved)
        print(f"permbank: {permBank2}")  ### TEST!!!
        print(f"tempbank: {tempBank1}")

        chooseTurn(player3, tempBank3, permBank3, puzzleSolved)
        print(f"permbank: {permBank3}")  ### TEST!!!
        print(f"tempbank: {tempBank1}")

        puzzleSolved = True
        
    roundCounter += 1

## Call round 3
# def round3():
