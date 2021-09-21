########################################################################
##
## CS 101 Lab
## Program #3
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that can guess numbers based on given numbers three remainders
##
## ALGORITHM : 
##      1. Set program with in a play again loop
##      2. Get first remainder and check if it is viable
##      3. Get second and third remainder and cross check their viability
##      4. Run a for loop to check possible integers 1 to 100\
##      5. Print integer with matching integ
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

print(
    '~Welcome User! To The GREAT Flarsheim Number Guesser!!!\n'
    'Please choose a number from 1 to 100 in your head\n'
    "Once you have your number I'm going to need you to answer a few simple questions\n")
playagain = 'Y'
while playagain == 'Y' or playagain == 'y':
    remain3 = int(input('What is the remainder of your number divided by 3?\n'))
    while remain3 != 0 and remain3 != 1 and remain3 != 2:
        if remain3 < 0:
            print('The remainder must be greater than 0')
        elif remain3 >= 3:
            print('The remainder must be less than 3')
        else:
            print('Unexpected input error')
        print('\nPlease enter a valid input')
        remain3 = int(input('What is the remainder of your number divided by 3?\n'))
    remain5 = int(input('What is the remainder of your number divided by 5?\n'))
    remain7 = int(input('What is the remainder of your number divided by 7?\n'))
    while remain5 == remain7:
        print('\nThe program has detected a calculation error, \nplease input the correct remainders')
        remain5 = int(input('What is the remainder of your number divided by 5?\n'))
        remain7 = int(input('What is the remainder of your number divided by 7?\n'))
    for i in range (1, 101):
        r3 = False
        r5 = False
        r7 = False
        if i % 3 == remain3:
            r3 = True
        if i % 5 == remain5:
            r5 = True
        if i % 7 == remain7:
            r7 = True
        while r3 and r5 and r7:
            print('Your number is',i)
            print('Pretty cool right?')
            break
    while 1 > 0:
        playagain = input('Do you want to play again? Y to continue, N to quit:\n')
        if playagain == 'y' or playagain == 'Y':
            break
        if playagain == 'n' or playagain == 'N':
            break