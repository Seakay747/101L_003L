########################################################################
##
## CS 101 Lab
## Program #11
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that uses the class object to keep time
##
## ALGORITHM : 
##      1. Set up the class Clock and the initialization
##      2. Set up the tick function within Clock to increment time
##      3. Take the time from the user
##      4. Use the time module to build an infinite loop that runs every second and prints time using the tic function
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##              
########################################################################  

import time

class Clock:
    def __init__(self, hour=0, minute=0, second=0, type=0):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        self.type = int(type)
        self.meridian = ''
        self.boolean = False
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = self.second - 60
            self.minute += 1
        if self.minute >= 60:
            self.minute = self.minute - 60
            self.hour +=1
        if self.hour > 24:
            self.hour = self.hour - 24
            if self.boolean:
                self.boolean = False
        if self.type == 1 and self.hour < 12:
            self.meridian = 'am'
        if self.type == 1 and self.hour == 12:
            self.meridian = 'pm'
        if self.type == 1 and self.hour > 12:
            self.hour = self.hour - 12
            self.boolean = True
        print('{:0>2}:{:0>2}:{:0>2} {:<2}'.format(self.hour, self.minute, self.second, self.meridian))
        if self.boolean:
            self.hour += 12

user_hours = int(input('\nEnter the current hour:\n'))
user_minutes = int(input('\nEnter the current minute:\n'))
user_seconds = int(input('\nEnter the current second:\n'))

clock = Clock(user_hours, user_minutes, user_seconds, 1)

while True:
    clock.tick()
    time.sleep(1)