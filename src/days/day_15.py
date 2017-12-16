from itertools import *


inp = {
    'Generator A': 722,
    'Generator B': 354,
}


def day_15_generate(gen):
    cur = gen['start']
    while True:
        cur = cur * gen['factor'] % 2147483647
        if cur % gen['yield_multiples_of'] == 0:
            yield cur & 0xFFFF


def day_15(inp=inp, pairs=40000000, yield_multiples_of={}):
    factor = {
        'Generator A': 16807,
        'Generator B': 48271,
    }

    generators = list(map(day_15_generate, [{
        'name': name,
        'start': start,
        'factor': factor[name],
        'yield_multiples_of': yield_multiples_of.get(name, 1),
    } for name, start in inp.items()]))

    match = sum(map(
        lambda r: r.count(r[0]) == len(r),
        islice(zip(*generators), pairs)
    ))

    return {
        'stats': '',
        'result': match,
    }


def day_15_part_2(inp=inp):
    ret = day_15(inp, pairs=5000000, yield_multiples_of={
        'Generator A': 4,
        'Generator B': 8,
    })
    return ret

