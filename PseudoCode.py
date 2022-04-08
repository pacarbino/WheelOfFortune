# = rules
## = pseudocode

# rules:
# rounds 1 and 2:

## create list of words to choose from
## create list of wheel spaces to choose from
## create blanks (gameboard) list
## create letters guessed list

## create bank for player 1
## create bank for player 2
## create bank for player 3

## create random word generator using word list
## create random wheel space generator from list

# puzzle of letters presented:
    ## call random word generator
    ## print display of word in "blanks" list

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
                    ## solve 
                    ## buy a vowel

            # 1) spin 
                ## call random wheel space generator
                    ## "spin" = result of function call above
                    ## if spin = prize:
                        ## ask for user input regarding letter choice
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
                                ## append words guessed list
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
# puzzle presented:
# default free letters given [r,s,t,l,n,e]
    # if letters above are in puzzle, they're shown in place
# player picks 3 more consonants and one more vowel
    # if letters above are in puzzle, they're shown in place
# player guesses puzzle (one chance)
    # if right, player wins mystery prize
    # if incorrect, player does not win mystery prize

    