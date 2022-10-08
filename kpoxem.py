import numbers
import time

print('enter time')
hours = input('hours: ')
minutes = input('minutes: ')
seconds = input('seconds: ')
while True:
    if len(hours) < 2:
        hours = '0' + hours
    if len(minutes) < 2:
        minutes = '0' + minutes
    if len(seconds) < 2:
        seconds = '0' + seconds

    int_h = int(hours)
    int_m = int(minutes)
    int_s = int(seconds)

    seconds_in_total = int_h * 3600 + int_m * 60 + int_s

    hours_for_print = numbers.ten_segment_num(hours)
    minutes_for_print = numbers.ten_segment_num(minutes)
    seconds_for_print = numbers.ten_segment_num(seconds)

    split_hours = hours_for_print.splitlines()
    split_minutes = minutes_for_print.splitlines()
    split_seconds = seconds_for_print.splitlines()

    res1 = split_hours[0] + '     ' + split_minutes[0] + '     ' + split_seconds[0]
    res2 = split_hours[1] + '  *  ' + split_minutes[1] + '  *  ' + split_seconds[1]
    res3 = split_hours[2] + '  *  ' + split_minutes[2] + '  *  ' + split_seconds[2]

    print(res1)
    print(res2)
    print(res3)

    if seconds_in_total == 0:
        print('              DONE               ')
        break

    int_s -= 1
    seconds = str(int_s)
    if int_s == -1:
        int_m -= 1
        minutes = str(int_m)
        int_s = 59
        seconds = str(int_s)
    if int_m == -1:
        int_h -= 1
        hours = str(int_h)
        int_m = 59
        minutes = str(int_m)

    time.sleep(1)
