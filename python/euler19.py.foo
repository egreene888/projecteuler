"""
euler21.py

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""

date = [1900, 1] # Date as a [Y, M], indexing from one
day = 0 # Day of the week, where 0 is Monday and 6 is Sunday.

answer = 0

while date[0] < 2001:
    if date[1] in [9, 4, 6, 11]: # thirty day months.
        date[1] += 1
        day += 30
    elif date[1] in [1, 3, 5, 7, 8, 10, 12]: # thirdy-one day months
        date[1] += 1
        day += 31
    elif date[1] == 2:
        date[1] += 1
        if date[0] % 4 == 0 and (date[0] % 100 != 0 or date[0] % 400 == 0):
            # in leap years
            day += 29
        else:
            day += 28

    # set the rollover for month and years
    if date[1] == 13:
        date[0] += 1
        date[1] = 1

    # set the day
    day %= 7

    # add to the counter
    if day == 6:
        if date[0] <= 2000 and date[0] >= 1901:
            answer += 1

print answer
