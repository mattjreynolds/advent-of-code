import itertools


with open('input/input_day_12.txt', 'r+') as f:
    inp = f.read()


def day_12_get_groups(p, prgs, processed):
    prg = prgs[p]
    links = prg['links'] - processed
    processed.update(prg['groups'])
    for l in links:
        prg['groups'].update(day_12_get_groups(
            l, prgs, processed=processed
        ))
    return prg['groups']


def day_12(inp=inp):
    lines = [l.strip() for l in inp.splitlines()]
    prgs = {}

    for l in lines:
        p, links = l.split(' <-> ')
        p = int(p)
        links = [int(l) for l in links.split(', ')]
        prgs[p] = {
            'links': set(links),
            'groups': set([p] + links),
        }

    for p in prgs.keys():
        day_12_get_groups(p, prgs, set())

    group_0 = len(prgs[0]['groups'])

    groups = [p['groups'] for p in prgs.values()]
    unique_groups = set(''.join(str(i) for i in sorted(list(g))) for g in groups)
    
    return {
        'stats': '',
        'result': group_0,
        'unique_groups': len(unique_groups),
    }


def day_12_part_2(inp=inp):
    ret = day_12(inp=inp)
    ret['result'] = ret['unique_groups']
    return ret

