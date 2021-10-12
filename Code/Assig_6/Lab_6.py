########################################################################
##
## CS 101 Lab
## Program #6
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that creates and deconstructs ceaser ciphers
##
## ALGORITHM : 
##      1. Create functions to loop alphabet, shift ASCII values, and stitch together messages
##      2. Use functions to pass values from user and between eachother to decipher/cipher and stitch together the new messages
##      3. Create menu
##      4. Create block of code that uses functions
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def menu():
    '''Prints the menu for the program'''
    print(
    '{:^50}\n{:^50}\n{:~<50}\n\n{:=<25}{:=>25}\n\n{:=<25}{:=>25}\n\n{:=<25}{:=>25}\n\n{:~<50}\n'.format(
        'Welcome','to the GREAT Ceaser Cipher!','','[e]','> encode a message','[d]','> decode a message','[q]','> quit',''
    ))
def encode(boolean):
    '''This function will gather the message and the amount that the message's ASCII values will be shifted
    from the user; the boolean value passed by decipher() dictates whether the message will be
    decoded or encoded'''
    message = input('Enter the message you wish to encode:\n')
    encoder = int(input('Enter the number you wish to use as your cipher value:\n'))
    while not 1 <= encoder <= 25:
        print('You have entered an invalid cipher value, please enter a number between 1 and 25')
        encoder = int(input('Enter the number you wish to use as your cipher value:\n'))
    if boolean:
        return message, (encoder * -1)
    else:
        return message, encoder
def alphabet_loop(a,b,order,encoder):
    '''Takes the parameters 'a' and 'b' to set the bounds for the allowed
    ranges of ASCII values, with the parameter 'order' and 'encoder' being used to
    find the new ASCII value that will be assessed. If the new ASCII value falls above the range,
    it will loop back to the lowest ASCII values and vice versa. The ASCII value is then converted back
    into a character and then returned'''
    new_order = order + encoder
    if new_order < a:
        new_order = (b + 1) - (a - new_order)
    if new_order > b:
        new_order = (new_order - b) + (a - 1)
    if new_order < a:
        new_order = (b + 1) - (a - new_order)
    new_char = chr(new_order)
    return new_char
def decipher(boolean):
    '''Takes the 'boolean' parameter to pass to the encode() function which.
    The message recieved from the encode() function is broken into a list of characters 
    which are then turned into ASCII values. These ASCII values are shifted the specified amount 
    and kept within the ASCII alphabet by the alphabet_loop() function. 
    After each character is shifted, it is stitched back into an empty string which is returned 
    after all the characters are shifted'''
    cipher = ''
    message, encoder = encode(boolean)
    char_list = list(message)
    for ele in char_list:
        if 65 <= ord(ele) <= 90:
            new_char = alphabet_loop(65,90,ord(ele),int(encoder))
            cipher += new_char
        elif 97 <= ord(ele) <= 122:
            new_char = alphabet_loop(97,122,ord(ele),int(encoder))
            cipher += new_char
        else:
            cipher += ele
    return message, cipher
loop = True
menu()
user_input = input('Please enter your choice:\n')
user_input = user_input.lower()
if user_input == 'q':
  loop = False
while loop:
    if user_input == 'e':
        message, cipher = decipher(False)
        print('Original Message: {}\nEncoded Message: {}\n'.format(message, cipher))
    elif user_input == 'd':
        message, cipher = decipher(True)
        print('Encoded Message: {}\nDeciphered Message: {}\n'.format(message, cipher))
    else:
      print('Please enter a valid menu option (e, d, or q)\n')
    menu()
    user_input = input('Please enter your choice:\n')
    user_input = user_input.lower()
    if user_input == 'q':
        loop = False