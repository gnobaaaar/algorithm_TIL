JAN, MAR, MAY, JUR, AUG, OCT = 31, 31, 31, 31, 31,31
APR, JUN, SEP, NOV = 30, 30, 30, 30
FEB = 28

month, day = input().split()

if month == '1':
    day = int(day) % 7
elif month == '2':
    day = (JAN + int(day)) % 7
elif month == '3':
    day = (JAN+FEB + int(day)) % 7
elif month == '4':
    day = (JAN+FEB+MAR + int(day)) % 7
elif month == '5':
    day = (JAN+FEB+MAR+APR + int(day)) % 7
elif month == '6':
    day = (JAN+FEB+MAR+APR+MAY + int(day)) % 7
elif month == '7':
    day = (JAN+FEB+MAR+APR+MAY+JUN + int(day)) % 7
elif month == '8':
    day = (JAN+FEB+MAR+APR+MAY+JUN+JUR + int(day)) % 7
elif month == '9':
    day = (JAN+FEB+MAR+APR+MAY+JUN+JUR+AUG + int(day)) % 7
elif month == '10':
    day = (JAN+FEB+MAR+APR+MAY+JUN+JUR+AUG+SEP + int(day)) % 7
elif month == '11':
    day = (JAN+FEB+MAR+APR+MAY+JUN+JUR+AUG+SEP+OCT + int(day)) % 7
elif month == '12':
    day = (JAN+FEB+MAR+APR+MAY+JUN+JUR+AUG+SEP+OCT+NOV + int(day)) % 7

if day == 1:
    print('MON')
elif day == 2:
    print('TUE')
elif day == 3:
    print('WED')
elif day == 4:
    print('THU')
elif day == 5:
    print('FRI')
elif day == 6:
    print('SAT')
else:
    print('SUN')