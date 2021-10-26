########################################################################
##
## CS 101 Lab
## Program #8
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that organizes, updates, and displays grade info using lists
##
## ALGORITHM : 
##      1. Make functions that preform the necessary math
##      2. Create if, elif, else ladder with error handling to run program
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##              
########################################################################      
import math
def extremes(l):
    '''finds the largest and smallest number from the list argument and returns them as a tuple'''
    mini = min(l)
    maxi = max(l)
    return maxi, mini
def average(l):
    '''finds the average of the given list argument'''
    sum = 0
    for ele in l:
        sum += ele
    avg = sum / len(l)
    return avg
def standard_dev(l):
    '''finds the standard deviation of  the given list argument'''
    avg = average(l)
    sum = 0
    for ele in l:
        sum += ((ele - avg) ** 2)
    std = math.sqrt((sum/len(l)))
    return std
def menu():
    '''prints the options menu'''
    print(
        '\n{:=^40}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n{:-<20}{:->20}\n'.format(
            'Grade Menu','1','Add Test','2','Remove Test','3','Clear Tests','4','Add Assignments','5','Remove Assignments','6','Clear Assignments','D','Display Scores','Q','Quit'))
def display(tests,programs):
    '''calculates and displays all given information given two lists as arguments routing to other functions to do the majority of the calculation'''
    print('\n{:<20}{:<8}{:<8}{:<8}{:<8}{}'.format('Type','#','min','max','avg','std'))
    print('='*60)
    tmax, tmin = extremes(tests)
    pmax, pmin = extremes(programs)
    print('{:<20}{:<8}{:<8}{:<8}{:<8.2f}{:.2f}'.format('Tests',len(tests),tmin,tmax,average(tests),standard_dev(tests)))
    print('{:<20}{:<8}{:<8}{:<8}{:<8.2f}{:.2f}\n'.format('Tests',len(programs),pmin,pmax,average(programs),standard_dev(programs)))
    print('The weighted score is {:.2f}'.format((average(tests) * 0.6) + (average(programs) * 0.4)))

tests = []
programs = []
menu()
user_input = input('Enter your menu selection:\n')
while user_input != 'Q' and user_input != 'q':
    try:   
        if user_input == '1':
            score = float(input('Enter the new Test score 0-100 ==> '))
            while score < 0:
                print('Negative scores cannot be entered')
                score = float(input('Enter the new Test score 0-100 ==> '))
            tests.append(score)
        elif user_input == '2':
            score = float(input('Enter the Test score to remove ==> '))
            tests.remove(score)
        elif user_input == '3':
            tests.clear()
            print('Tests was cleared')
        elif user_input == '4':
            score = float(input('Enter the new Assignment score 0-100 ==> '))
            while score < 0:
                print('Negative scores cannot be entered')
                score = float(input('Enter the new Assignment score 0-100 ==> '))
            programs.append(score)
        elif user_input == '5':
            score = float(input('Enter the Assignment score to remove ==> '))
            programs.remove(score)
        elif user_input == '6':
            programs.clear()
            print('Assignments was cleared')
        elif user_input == 'D' or user_input == 'd':
            display(tests,programs)
        else:
            user_input = input('The input you entered was invalid, please enter an option from the menu:\n')
        menu()
        user_input = input('Enter your menu selection:\n')
    except(TypeError):
        print('Scores must be entered as intergers, please try again')
    except(ValueError):
        print('The score {} was not found'.format(score))