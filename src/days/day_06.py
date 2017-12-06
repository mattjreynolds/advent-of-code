inp = '''2 8 8 5 4 2 3 1 5 5 1 2 15 13 5 14'''

import itertools


def jump(index, search):
    idx = None
    while idx != search:
        idx = next(index)
    return idx

def day_06(inp=inp):
    banks = [int(i) for i in inp.split()]

    idx = 0
    most = 0
    states = []
    counter = itertools.count()
    index = itertools.cycle(range(0,len(banks)))

    while banks not in states:
        states.append(banks.copy())
        count = next(counter)
        
        most = max(banks)
        idx = jump(index, banks.index(most))
        banks[idx] = 0
        
        while most:
            idx = next(index)
            most -= 1 
            banks[idx] += 1

    states.append(banks.copy())
    count = next(counter)

    return {
        'stats': '',
        'result': count,
        'states': states,
    }


def day_06_part_2(inp=inp):
    ret = day_06(inp=inp)
    ret['result'] = len(ret['states']) - 1 - ret['states'].index(ret['states'][-1])
    return ret

