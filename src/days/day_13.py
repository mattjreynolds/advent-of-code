import itertools
from pprint import pprint

with open('input/input_day_13.txt', 'r+') as f:
    inp = f.read()


def day_13(inp=inp, find_delay=False):
    lines = [l.strip() for l in inp.splitlines()]

    layers = {
        int(k): {
            'depth': int(k),
            'range': int(v),
            'hits': itertools.count(0, 2*int(v)-2),
            'scan_range': itertools.cycle(list(range(0,int(v)))+list(range(int(v)-2,0,-1))),
            'scan_pos': 0,
        } for k,v in [l.split(': ') for l in lines]
    }

    pos = 0
    delay = 0
    severity = 0
    caught = False

    if find_delay:
        all_hits = set()
        last_min_hit = 0
        for _ in itertools.count():
            for depth, details in layers.items():
                details['hit'] = next(details['hits'])
            hits = [d['hit']-d['depth'] for d in layers.values()]
            pos_hits = [h for h in hits if h >= 0]
            all_hits.update(pos_hits)
            min_hit = min(pos_hits)
            for i in range(last_min_hit, min_hit+1):
                if i not in all_hits:
                    delay = i
                    break
            last_min_hit = min_hit
            if delay:
                break
    else:
        for step in range(pos, 1+max(layers.keys())):
            for depth, details in layers.items():
                details['scan_pos'] = next(details['scan_range'])

            if layers.get(step, {}).get('scan_pos') == 0:
                caught = True
                layers[step]['caught'] = True
                severity += step * layers[step]['range']

    return {
        'stats': '',
        'result': severity,
        'caught': caught,
        'delay': delay,
    }


def day_13_part_2(inp=inp):
    ret = day_13(inp=inp, find_delay=True)
    ret['result'] = ret['delay']
    return ret

