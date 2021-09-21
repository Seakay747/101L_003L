## CS 101 Lab
## Program #2
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Automate a way to have students check their weighted grade
##
## ALGORITHM : 
##      1. define a function to insure the grade falls between 0 and 100
##      2. gather user name and grades (call funtion to check grades)
##      3. calculate weighted grade
##      4. set up if, elif, else chain to designate a letter grade to the weighted grade
##      5. output weighted grade and letter grade
## 
## ERROR HANDLING:
##      Do not enter strings for grades
##
## OTHER COMMENTS:
##      N/A
print('**** Welcome to the LAB grade calculator! ****')
user_name = input('\nWho are we calculating grades for? => ')
lab_grade = int(input('\nEnter your Lab grade => '))
if lab_grade > 100:
  lab_grade = 100
  print('The grade input should be 100 or less.\nIt has been changed to 100.')
if lab_grade < 0:
  lab_grade = 0
  print('The grade input should be 0 or greater.\nIt has been chnaged to 0.')
exam_grade = int(input('\nEnter your Exam grade => '))
if exam_grade > 100:
  exam_grade = 100
  print('The grade input should be 100 or less.\nIt has been changed to 100.')
if exam_grade < 0:
  exam_grade = 0
  print('The grade input should be 0 or greater.\nIt has been chnaged to 0.')
attendance_grade = int(input('\nEnter your attendance grade => '))
if attendance_grade > 100:
  attendance_grade = 100
  print('The grade input should be 100 or less.\nIt has been changed to 100.')
if attendance_grade < 0:
  attendance_grade = 0
  print('The grade input should be 0 or greater.\nIt has been chnaged to 0.')
lab = lab_grade * 0.7
exam = exam_grade * 0.2
attendance = attendance_grade * 0.1
weight_grade = lab + exam + attendance
if weight_grade >= 90:
  letter = 'A'
elif weight_grade >= 80:
  letter = 'B'
elif weight_grade >= 70:
  letter = 'C'
elif weight_grade >= 60:
  letter = 'D'
else:
  letter = 'F'
print('\nThe weighted grade for',user_name,'is',weight_grade)
print(user_name,'has a letter grade of',letter)