def ten_segment_num(number):
    rows = [''] * 3

    for i, digit in enumerate(number):
        if digit == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif digit == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif digit == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif digit == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif digit == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif digit == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif digit == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif digit == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif digit == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif digit == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

    return '\n'.join(rows)
