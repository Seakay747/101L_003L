########################################################################
##
## CS 101 Lab
## Program #9
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that organizes, updates, and displays grade info using lists
##
## ALGORITHM : 
##      1. Make functions that preform the necessary dictionary creation and file reading
##      2. Use and sort the data from said dictionaries to fill out print statements
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##              
######################################################################## 
import csv
def month_from_number(month):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
    if not 1 <= month <= 12:
        raise ValueError('Month must be 1-12')
    month -= 1
    output = months[month]
    return output
def read_in_file(read_file):
    lines_lib = []
    with open(read_file, 'r') as csvf:
        for i, line in enumerate(csv.reader(csvf)):
            lines_lib.append(line)
    return lines_lib
def create_reported_date_dict(lines_lib):
    date_dict = {}
    first_line = True
    for line in lines_lib:
        if first_line:
            first_line = False
            continue
        if line[1] in date_dict:
            try:
                date_dict[line[1]] += 1
            except KeyError:
                date_dict[line[1]] = 1
        else:
            date_dict[line[1]] = 1
    return(date_dict)
def create_reported_month_dict(lines_lib):
    month_dict = {}
    first_line = True
    for line in lines_lib:
        if first_line:
            first_line = False
            continue
        if int(line[1][0:2]) in month_dict:
            try:
                month_dict[int(line[1][0:2])] += 1
            except KeyError:
                month_dict[int(line[1][0:2])] = 1
        else:
            month_dict[int(line[1][0:2])] = 1
    return month_dict
def create_offense_dict(lines_lib):
    offense_dict = {}
    first_line = True
    for line in lines_lib:
        if first_line:
            first_line = False
            continue
        if str(line[7].split(' – ')[0]) in offense_dict:
            try:
                offense_dict[str(line[7].split(' – ')[0])] += 1
            except KeyError:
                offense_dict[str(line[7].split(' – ')[0])] = 1
        else:
            offense_dict[(line[7].split(' – ')[0])] = 1
    return(offense_dict)
def create_offense_by_zip_dict(lines_lib):
    offense_by_zip_dict = {}
    first_line = True
    for line in lines_lib:
        if first_line:
            first_line = False
            continue
        if str(line[7].split(' – ')[0]) in offense_by_zip_dict:
            if line[13] in offense_by_zip_dict[str(line[7].split(' – ')[0])]:
                offense_by_zip_dict[str(line[7].split(' – ')[0])][line[13]] += 1
            else:
                offense_by_zip_dict[str(line[7].split(' – ')[0])][line[13]] = 1
        else:
            offense_by_zip_dict[str(line[7].split(' – ')[0])] = {line[13]:1}
    return(offense_by_zip_dict)
        
loop =True
while loop:
    user_file = input('Enter the name of the crime data file:\n')
    try:
        lines_lib = read_in_file(user_file)
        loop = False
    except FileNotFoundError:
        print('Could not find the file {}'.format(user_file))

reported_date = create_reported_date_dict(lines_lib)
reported_month = create_reported_month_dict(lines_lib)
offense = create_offense_dict(lines_lib)
offense_by_zip = create_offense_by_zip_dict(lines_lib)

hi_crime_month = dict(sorted(reported_month.items(), key=lambda x:x[1], reverse = True))
hi_crime_offense = dict(sorted(offense.items(), key=lambda x:x[1], reverse = True))
print('\nThe month with the highest # of crimes is {} with {} offenses'.format(month_from_number(list(hi_crime_month.keys())[0]),list(hi_crime_month.values())[0]))
print('The offense with the highest # of offenses is {} with {} offenses'.format(list(hi_crime_offense.keys())[0],list(hi_crime_offense.values())[0]))

loop = True
while loop:
    user_offense = input('\nEnter and offense:\n').title()
    if user_offense in offense_by_zip:
        print(user_offense,'by Zip Code')
        print('{:<5}{:>47}'.format('Zip Code','# of Offenses'))
        print('='*55)
        for key in offense_by_zip[user_offense]:
            print('{:<5}{:>50}'.format(key,offense_by_zip[user_offense][key]))
        loop = False
    else:
        print('{} is not a valid offense, please try again'.format(user_offense))