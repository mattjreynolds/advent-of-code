import math
import itertools
from collections import defaultdict
# from pprint import pprint


inp = 325489


def sum_adjacent_squares(matrix, i):
    if i == 1:
        return 1

    neighbours = {
        k:v for k,v in matrix.items() 
        if (
            k < i
            and abs(v['x']-matrix[i]['x']) < 2
            and abs(v['y']-matrix[i]['y']) < 2
        )
    }

    return sum(n['value'] for n in neighbours.values())

def generate_matrix(inp=inp, stress_test=False):
    values = [{
        'value': 1,
        'x': 0,
        'y': 0,
    }]

    matrix = defaultdict(dict)
    xy = {'x': 0, 'y': 0}
    distance = itertools.count()
    direction = itertools.cycle(['r', 'u', 'l', 'd'])
    coords = {
        'r': {'x': 1, 'y': 0},
        'u': {'x': 0, 'y': 1},
        'l': {'x':-1, 'y': 0},
        'd': {'x': 0, 'y':-1},
    }

    dist = next(distance)
    dist_ctr = 0
    move = coords[next(direction)]

    for i in range(1, inp+1):
        matrix[i].update(xy)
        value = sum_adjacent_squares(matrix, i) if stress_test else i
        matrix[i]['value'] = value
        
        # print(f'{i}, {xy}, {dist_ctr}/{dist}, {move}')

        if math.sqrt(i).is_integer():
            dist = next(distance)

        if dist_ctr == dist:
            dist_ctr = 0
            move = coords[next(direction)]

        dist_ctr += 1
        xy['x'] += move['x']
        xy['y'] += move['y']

    # pprint(matrix)
    return matrix


def day_03(inp=inp):
    matrix = generate_matrix(inp)

    distance = abs(matrix[inp]['x']) + abs(matrix[inp]['y'])

    return {
        'stats': '',
        'result': distance,
    }


def day_03_part_2(inp=inp):
    matrix = generate_matrix(inp=inp+1, stress_test=True)
    
    print(matrix[inp+1]['value'])
    value = matrix[inp]['value']

    return {
        'stats': '',
        'result': value,
    }
