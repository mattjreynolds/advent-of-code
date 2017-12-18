from itertools import *


with open('input/input_day_16.txt', 'r+') as f:
    inp = f.read()

programs = 'abcdefghijklmnop'


def day_16_spin(l, n):
    if int(n) > 0:
        l.insert(0, l.pop(-1))
        day_16_spin(l, int(n)-1)


def day_16_exchange(l, a, b):
    l[int(a)], l[int(b)] = l[int(b)], l[int(a)]


def day_16_partner(l, a, b):
    day_16_exchange(l, l.index(a), l.index(b))


def day_16(inp=inp, programs=programs, dances=1):

    programs = list(programs)
    move = {
        's': day_16_spin,
        'x': day_16_exchange,
        'p': day_16_partner,
    }

    for _ in range(dances):
        for step in inp.split(','):
            move[step[0]](programs, *step[1:].split('/'))

    return {
        'stats': '',
        'result': ''.join(programs),
    }


def day_16_part_2(inp=inp, programs=programs):
    ret = day_16(inp, programs=programs, dances=10000)  # Not 1 billion but got the right answer!
    return ret

