########################################################################
##
## CS 101 Lab
## Program #4
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a gambling program that tracks bank balance and rolls slots
##
## ALGORITHM : 
##      1. define functions to do specific actions
##      2. call functions to set balances
##      3. call functions to spin, calculate gain/loss, and then loop
##      4. when loop ends call play again
## 
## ERROR HANDLING:
##      Do not enter strings for any integer calls
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import random
def play_again():
    user_input = input('Do you want to play again?\n')
    user_input = user_input.upper()
    while user_input != 'Y' and user_input != 'YES' and user_input != 'N' and user_input != 'NO':
        print('You must enter Y/YES/N/NO to continue. Please try again')
        user_input = input('Do you want to play again?\n')
        user_input = user_input.upper()
    if user_input == 'Y' or user_input == 'YES':
        return True
    if user_input == 'N' or 'NO':
        return False
def get_wager(bank):
    repeat = True
    while repeat:
        wager = int(input('How many chips do you want to wager?\n'))
        if wager <= 0:
            print('The wager must be greater than 0. Please try again.')
        elif wager > bank:
            print('The wager cannot be greater than the amount in your bank:', bank)
        else:
            repeat = False
    return wager
def get_slot_results():
    reela = random.randint(1, 11)
    reelb = random.randint(1, 11)
    reelc = random.randint(1, 11)
    return reela, reelb, reelc
def get_matches(reeltuple):
    reela = reeltuple[0]
    reelb = reeltuple[1]
    reelc = reeltuple[2]
    matches = 0
    if reela == reelb or reelb == reelc or reela == reelc:
        matches = 2
    if reela == reelb == reelc:
        matches = 3
    return matches
def get_bank():
    repeat = True
    while repeat:
        chips = int(input('How many chips do you want to start with?\n'))
        if chips <= 0:
            print('Too low of a value, you can only choose 1-100 chips.')
        elif chips > 100:
            print('Too high of a value, you can only choose 1-100 chips.')
        else:
            repeat = False
    return chips
def get_payout(wager, matches):
    if matches == 3:
        payout = wager * 9
    elif matches == 2:
        payout = wager * 2
    else:
        payout = -1 * wager
    return payout

if __name__ == "__main__":

    repeat = True
    losses = 0
    spins = 0
    max_bank = 0
    while repeat:
        bank = get_bank()
        while bank > 0:
            if bank >= max_bank:
                max_bank = bank
            wager = get_wager(bank)
            reeltuple = get_slot_results()
            print('Your spin {} {} {}'.format(reeltuple[0], reeltuple[1], reeltuple[2]))
            matches = get_matches(reeltuple)
            print('You matched {} reels'.format(matches))
            payout = get_payout(wager, matches)
            print('You won/lost',payout)
            if payout < 0:
                losses += 1
            spins += 1
            bank += payout
            print('Current bank:',bank)
        print("\nYou lost {} in {} spins".format(losses, spins))
        print("The most chips you had was {}".format(max_bank))
        repeat = play_again()