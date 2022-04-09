#rules:
# rounds 1 and 2:

# puzzle of letters presented:
# 3 players
# everyone starts with $0
# player 1 turn:
    # if player has money, choose to:
        # spin 
        # buy a vowel
        # solve puzzle
    # if player has NO money
        # solve puzzle
        # spins
            # if "good" spin:
                # guess consonant [i]
                    # if [i] correct:
                        # win $$*[i] instances in word
                        # repeat spin until wrong guess or "bad" spin
                        # or buy a vowel
                        # or choose to solve
                    # if incorrect:
                        # player's turn ends
            # if lose a turn:
                # player loses a turn (makes no guesses)
            # if bankrupt:
                # player loses all money won in round
                # player loses turn (makes no guesses)
# player 2 spins and repeats process
# player 3 spins and repeats process
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

    