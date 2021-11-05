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
##      1. Read in file as lists, make on list of lists, make string of lists, make list of char in string, use ascii vals to remove punc
##      2. Create dict of words and their frequency, use enumerate to format printed menu
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##              
######################################################################## 
user_file = input('Enter of the name of the file to open:\n')
loop = True
while loop:
    try:
        with open(user_file, 'r') as f:
            file_lines = f.readlines()
        loop = False
    except:
        print('The file {} could not be found, please enter a valid file name'.format(user_file))
        user_file = input('Enter of the name of the file to open:\n')
file_text = ''
temp_list = []
for ele in file_lines:
    temp = ele.split()
    temp_list.extend(temp)
word_string = ''
for ele in temp_list:
    word_string += ele
    word_string += ' '
word_string = word_string.lower()
output_string = ''
for ele in list(word_string):
    if 97 <= ord(ele) <= 122 or ord(ele) == 32:
        output_string += ele
words_list = output_string.split()
word_count_dict = {}
for ele in words_list:
    if ele in word_count_dict:
        word_count_dict[ele] += 1
    else:
        word_count_dict[ele] = 1
word_freq_dict = dict(sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True))
only_once = 0
for key in word_freq_dict:
    if word_freq_dict[key] == 1:
        only_once += 1
print('\nThere are {} words that occur only once'.format(only_once))
print('There are {} unique words'.format(len(word_freq_dict)))
print('{:<3}{:>20}{:>12}'.format('#','Word','Freq.'))
print('='*35)
for i, key in enumerate(word_freq_dict):
    print('{:<3}{:>20}{:>12}'.format(i+1,key,word_freq_dict[key]))