########################################################################
##
## CS 101 Lab
## Program #5
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a library card checker program
##
## ALGORITHM : 
##      1. define functions to break down complexity
##      2. call functions to verify the aspects of the card number
##      3. print statements returned by function tuples
##      4. add loop and loop checker based on boolean values
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def print_menu():
    print('{:^50}\n{:^50}\n{:=<50}\n'.format('Linda Hall','Library Card Check',''))
def char_val(char):
    char = char.upper()
    char_index = ord(char) - 65
    return char_index
def get_check_digit(user_string):
    list1 = list(user_string)
    list1.pop(-1)
    index = 1
    sum = 0
    for ele in list1:
        if 65 <= ord(ele) <= 90:
            ele = char_val(ele)
        else:
            ele = int(ele)
        sum += ele * index
        index += 1
    check_digit = sum % 10
    return check_digit
def verify_check_digit(user_string):
    check_digit = get_check_digit(user_string)
    list1 = list(user_string)
    if len(list1) != 10:
        return False, 'The length of the number given must 10'
    for i in range(0,5):
        if not 65 <= ord(list1[i]) <= 90:
            return False, 'The first 5 characters must be A-Z, the invalid character is at {} and is {}'.format(i, list1[i])
    for i in range(7, 10):
        if not 48 <= ord(list1[i]) <= 57:
            return False, 'The last 3 characters must be 0-9, the invalid character is at {} and is {}'.format(i, list1[i])
    if int(list1[5]) != 1 and int(list1[5]) != 2 and int(list1[5])!= 3:
        return False, 'The sixth character must be 1 2 or 3'
    if int(list1[6]) != 1 and int(list1[6]) != 2 and int(list1[6]) != 3 and int(list1[6]) != 4:
        return False, 'The seventh character must be 1 2 3 or 4'
    if check_digit != int(list1[9]):
        return False, 'Chack Digit {} does not match calculated value {}'.format(list1[9], check_digit)
    return True, ''
def get_school(user_string):
    list1 = list(user_string)
    if int(list1[5]) == 1:
        return 'School of Computing and Engineering SCE'
    elif int(list1[5]) == 2:
        return 'School of Law'
    elif int(list1[5]) == 3:
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
def get_grade(user_string):
    list1 = list(user_string)
    if int(list1[6]) == 1:
        return 'Freshman'
    elif int(list1[6]) == 2:
        return 'Sophomore'
    elif int(list1[6]) == 3:
        return 'Junior'
    elif int(list1[6]) == 4:
        return 'Senior'
    else:
        return 'Invalid Grade'

__name__ == '__main__'

print_menu()
loop = True
card_number = input('Enter Library Card. Hit Enter to Exit: ')
if card_number == '':
    loop = False
while loop:
    verify, statement = verify_check_digit(card_number)
    if verify:
        print('Library Card is Valid')
    else:
        print('Library Card is not Valid')
    if statement == '':
        school = get_school(card_number)
        grade = get_grade(card_number)
        print('The card belongs to a student in',school)
        print('The card belongs to a',grade)
    else:
        print(statement)
    print()
    card_number = input('Enter Library Card. Hit Enter to Exit: ')
    if card_number == '':
        loop = False