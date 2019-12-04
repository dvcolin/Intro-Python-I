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

current_year = datetime.now().year
current_month = datetime.now().month

user_input = input(
    'Enter month and year (optional) separated by a space: ').split(' ')


def generate_calendar(ui):
    if len(ui) == 1 and ui[0] == '':
        print(calendar.month(current_year, current_month))
    elif len(ui) == 1:
        try:
            monthInt = int(ui[0])
            print(calendar.month(2019, monthInt))
        except ValueError:
            print('Only numbers can be entered.')

    elif len(ui) == 2:
        try:
            monthInt = int(ui[0])
            yearInt = int(ui[1])
            print(calendar.month(yearInt, monthInt))
        except ValueError:
            print('Only numbers can be entered.')
    else:
        print('Only accepts two arguments.')


generate_calendar(user_input)
