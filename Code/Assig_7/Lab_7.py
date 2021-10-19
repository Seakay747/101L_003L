########################################################################
##
## CS 101 Lab
## Program #7
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that filters through an input file and pulls cars that meet a certain gas milage
##
## ALGORITHM : 
##      1. Take a gas milage, and infile, and an outfile from the user
##      2. Use try and except blocks to ensure the inputs are valid
##      3. Scan the documents to find cars that meet the requirements
##      4. Output the classes to the output doc
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##              
########################################################################                            
loop = True
while loop:
    try:
        mpg = int(input('Enter the minimum mpg:\n'))
        if mpg <= 0:
            print('Fuel economy must be greater than 0')
        elif mpg >= 100:
            print('Fuel economy must be less than 100')
        else:
            loop = False
    except:
        print('You must enter a number for fuel economy')
out_lib = []
loop = True
while loop:
    try:
        read_file = input('\nEnter the name of the input vehicle file:\n')
        with open(read_file, 'r') as f:
            contents = f.readlines()
            first_line = True
            for line in contents:
                try:
                    if first_line == True:
                        first_line = False
                        continue
                    temp = line.split('\t')
                    if int(temp[-3]) >= mpg:
                        out_string = '{:<5}{:<35}{:-<45}{:->20.3f}'.format(temp[0], temp[1], temp[2], int(temp[-3]))
                        out_lib.append(out_string)
                except:
                    print('\nCould not convert value {} for {} {}'.format(temp[-3], temp[0], temp[1]))
        loop = False
    except:
        print('Could not open file {}'.format(read_file))
loop = True
while loop:
    try:
        write_file = input('\nEnter the name of the file to output to\n')
        with open(write_file, 'w') as f:
            for ele in out_lib:
                f.write(ele)
                f.write('\n')
        loop = False
    except:
        print('There is an IO Error', write_file)