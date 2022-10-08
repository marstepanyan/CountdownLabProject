import numbers

print('enter time')
hours = input('hours: ')
minutes = input('minutes: ')
seconds = input('seconds: ')

new_hours = numbers.ten_segment_num(hours)
new_minutes = numbers.ten_segment_num(minutes)
new_seconds = numbers.ten_segment_num(seconds)

split_hours = new_hours.splitlines()
split_minutes = new_minutes.splitlines()
split_seconds = new_seconds.splitlines()

res1 = split_hours[0] + '     ' + split_minutes[0] + '     ' + split_seconds[0]
res2 = split_hours[1] + '  *  ' + split_minutes[1] + '  *  ' + split_seconds[1]
res3 = split_hours[2] + '  *  ' + split_minutes[2] + '  *  ' + split_seconds[2]

print(res1)
print(res2)
print(res3)


