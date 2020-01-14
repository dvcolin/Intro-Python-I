"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input = input(
    'Please enter a integer for month and year, separated by a space (optional): ').split(' ')

current_year = datetime.now().year
current_month = datetime.now().month

if len(user_input) == 1 and user_input[0] == '':
    print(calendar.month(current_year, current_month))

elif len(user_input) == 1 and user_input[0] != '':
    try:
        int(user_input[0])
        print(calendar.month(current_year, int(user_input[0])))
    except:
        print('Only integers are allowed.')
elif len(user_input) == 2 and user_input[0] != '' and user_input[1] != '':
    try:
        int(user_input[0])
        int(user_input[1])
        print(calendar.month(int(user_input[1]), int(user_input[0])))
    except:
        print('Only integers are allowed.')
else:
    print('Invalid command. Enter a maximum of two integers separated by a space.')
