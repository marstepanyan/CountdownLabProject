import numbers
import time


def countdown(s):

    while s >= 0:
        print(numbers.ten_segment_num(str(s)))
        time.sleep(1)

        s -= 1


# print(countdown(5))
