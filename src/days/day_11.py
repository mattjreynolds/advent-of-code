import itertools


with open('input/input_day_11.txt', 'r+') as f:
    inp = f.read()


def day_11_take_a_step(pos, step):
    for axis, dist in step.items():
        pos[axis] += dist


def day_11_ns_shortcut(pos):
    fn = None
    if pos['nesw'] > 0 and pos['nwse'] > 0:
        fn = min
    elif pos['nesw'] < 0 and pos['nwse'] < 0:
        fn = max
    if fn:
        mn = fn(pos['nesw'], pos['nwse'])
        pos['nesw'] -= mn
        pos['nwse'] -= mn
        pos['ns'] += mn
    return
    
    
def day_11_dist_to_loc(pos):
    day_11_ns_shortcut(pos)
    return sum((abs(x) for x in pos.values()))


def day_11(inp=inp):

    steps = inp.strip().split(',')
    pos = {
        'ns': 0,
        'nesw': 0,
        'nwse': 0,
    }
    move = {
        'nw': {'nwse': 1},
        'n': {'nesw': 1, 'nwse': 1},
        'ne': {'nesw': 1},
        'se': {'nwse': -1},
        's': {'nesw': -1, 'nwse': -1},
        'sw': {'nesw': -1},
    }
    max_dist = 0

    for s in steps:
        day_11_take_a_step(pos, move[s])
        max_dist = max(max_dist, day_11_dist_to_loc(pos.copy()))

    return {
        'stats': '',
        'max_dist': max_dist,
        'result': day_11_dist_to_loc(pos),
    }


def day_11_part_2(inp=inp):
    ret = day_11(inp=inp)
    ret['result'] = ret['max_dist']
    return ret

