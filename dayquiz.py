"""
A simple script for quizing yourself on the weekday that a given date falls on

Author: Jacob Dentes the maestro
Date: 5 December 2021 (Sunday (; )
"""

import datetime
import random

MONTHDAYS = (31,28,31,30,31,30,31,31,30,31,30,31)
WEEKDAYS = ('Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday')

def monthdays(month, year):
    """
    Returns the number of days in a given month

    Parameter month: an integer month, Jan. is 0 and Dec. is 11
    Precondition: month is an int and 0 <= month <= 11

    Parameter year: the year the month lies in
    Precondition: year is an int and year
    """
    assert isinstance(month, int) and 0 <= month <= 11
    assert isinstance(year, int) and 0 < year
    if year%4 == 0 and month==1:
        return 29
    return MONTHDAYS[month]

def day_str(day):
    """
    Returns the name of an integer day

    Parameter day: the integer day where Sunday is 0 and Saturday is 6
    Precondition: day is an int and 0 <= day <= 6
    """
    assert isinstance(day, int) and 0 <= day <= 6
    return WEEKDAYS[day]

def main():
    # Ask user to input date range
    chosen = False
    while not chosen:  # Lower bound loop
        lo = input('\nEnter a lower bound for years to guess: ')
        try:
            lo = int(lo)
            assert 9999 > lo > 0
            chosen = True
        except (ValueError, AssertionError):
            print('Enter a year as a positive integer less than 9999.')
    chosen = False
    while not chosen:  # Upper bound loop
        hi = input('Enter an upper bound for years to guess: ')
        try:
            hi = int(hi)
            assert 9999 > hi > 0
            chosen = True
        except (ValueError, AssertionError):
            print('Enter a year as a positive integer less than 9999.')

    playing = True
    # Game loop
    while playing:
        # Generate a random date
        year = random.randrange(lo,hi+1)
        month = random.randrange(1,13)
        days = monthdays(month-1,year)
        day = random.randrange(1,days+1)
        date = datetime.date(year,month,day)

        # Find weekday for that date
        weekday = (date.weekday() + 1)%7
        weekday_str = day_str(weekday)

        # Ask user what the day is
        print(f'\nWhat weekday was {str(date)}? (YEAR-MONTH-DAY)')
        print('You may write out the word or type an integer with 0 being Sunday and 6 being Saturday\n')
        guess = input('Enter the day: ')

        # Adjust guess if it is an integer
        if guess.isdigit():
            guess = int(guess)
            if 0 <= guess <= 6:
                guess = day_str(guess)
            else:
                guess = 'not a day.'

        # Tell user if they are correct
        if guess.lower() == weekday_str.lower():
            print('\nCorrect_B00MER! :)\n')
        else:
            print('\nIncorrect_haha_ID10t. :(\n')
        print(f'The answer was: {weekday_str}')
        print(f'Your guess was: {guess}\n')

        if input('Play again_intothedungeon? y/n: ') == 'n':
            playing = False

if __name__ == '__main__':
    main()
