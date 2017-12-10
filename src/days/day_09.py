with open('input/input_day_09.txt', 'r+') as f:
    inp = f.read()

import itertools


def day_09(inp=inp):

    skip_next = False
    comment  = False
    group_ptr = 0 
    group_count = 0
    group_scores = [0]
    garbage_count = 0

    for c in inp:
        if skip_next:
            skip_next = False
        else:
            if c == '!': 
                skip_next = True
            elif not comment and c == '<':
                comment = True
            elif c == '>':
                comment = False
            elif comment:
                    garbage_count += 1
            else:
                if c == '{': 
                    group_ptr += 1
                    group_count += 1
                    group_scores.append(group_ptr)
                elif c == '}':
                    group_ptr -= 1
                elif c == ',':
                    # group seperator
                    pass
                else:
                    # newline
                    pass

    return {
        'stats': '',
        'group_count': group_count,
        'garbage': garbage_count,
        'result': sum(group_scores),
    }


def day_09_part_2(inp=inp):
    ret = day_09(inp=inp)
    ret['result'] = ret['garbage']
    return ret

