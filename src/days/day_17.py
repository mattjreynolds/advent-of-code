from itertools import *


inp=359


def day_17(step=inp, stop=2017, search=2017):

    buf = [0]
    pos = 0

    for i in range(1, stop+1):
        pos = (pos+step) % i+1
        buf.insert(pos, i)
        
    return {
        'stats': '',
        'result': buf[buf.index(search)+1],
    }


def day_17_part_2(step=inp, stop=50000001, search=0):

    pos = 0
    final = None

    for i in range(1, stop+1):
        pos = (pos+step) % i+1
        if pos == search+1:
            final = i

    return {
        'stats': '',
        'result': final,
    }

