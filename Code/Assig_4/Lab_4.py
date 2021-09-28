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
    reela = random.randint(1, 10)
    reelb = random.randint(1, 10)
    reelc = random.randint(1, 10)
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
repeat = True
while repeat:
    bank = get_bank()
    while bank > 0:
        wager = get_wager(bank)
        reeltuple = get_slot_results()
        print('Your spin {} {} {}'.format(reeltuple[0], reeltuple[1], reeltuple[2]))
        matches = get_matches(reeltuple)
        print('You matched {} reels'.format(matches))
        payout = get_payout(wager, matches)
        print('You won/lost',payout)
        bank += payout
        print('Current bank:',bank)
    repeat = play_again()
