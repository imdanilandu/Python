def is_leap_year(y):
    if y % 4 == 0:
        print('год', y, ':', True)
    else:
        print('год', y, ':', False)

is_leap_year(2012)