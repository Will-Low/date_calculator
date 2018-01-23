from __future__ import print_function
from builtins import input
from os import system
import datetime

def run():
    '''Runs  script'''
    system('clear')
    start_input = input('Input starting date (mm/dd/yyyy) or;\n\nInterval '\
                        'from today [+/-][#][business days (b)/calendar '\
                        'days(c)/weeks(w)]\n\n>>> ')
    if start_input[0] in ('+', '-'):
        interval = int(start_input[0:len(start_input)-1])
        units = start_input[len(start_input)-1:]
        start_input = datetime.date.today()
    else:
        # string to date conversion
        start_input = datetime.datetime.strptime(start_input, '%m/%d/%Y')
        raw_interval = input('\nWhat interval are you calculating?\n\nFormat: '\
                             '[+/-][#][business days (b)/calendar(c)/weeks(w)]'\
                             '\n\n>>> ')
        interval = int(raw_interval[0:len(raw_interval)-1])
        units = raw_interval[len(raw_interval)-1:]

    # for calendar days
    if units == 'c':
        answer = start_input + datetime.timedelta(days=interval)
        print('\nYour calculated date is:', answer.strftime('%m/%d/%Y'), '\n')

    # for business days
    elif units == 'b':
        # renaming these variables for ease of reading
        biz_days_left = interval
        date_position = start_input
        while biz_days_left != 0:
            if biz_days_left > 0:
                date_position = date_position + datetime.timedelta(days=1)
                if date_position.weekday() < 5:
                    biz_days_left -= 1
                else:
                    continue
            elif biz_days_left < 0:
                date_position = date_position - datetime.timedelta(days=1)
                if date_position.weekday() < 5:
                    biz_days_left += 1
                else:
                    continue
        answer = date_position
        print('\nYour calculated date is:', answer.strftime('%m/%d/%Y'))
        print('\nFYI: This business-day calculator ignores holidays.\n'\
              'Consult business calendar for list of any relevant holidays.\n')

    # for weeks
    else:
        answer = start_input + datetime.timedelta(weeks=interval)
        print('\nYour calculated date is:', answer.strftime('%m/%d/%Y'), '\n')

    system('read -s -n 1 -p "Press any key to calculate another date..."')
    run()

run()
