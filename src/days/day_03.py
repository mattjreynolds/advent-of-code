import math
import numpy
import itertools
from collections import defaultdict


inp = 325489


def sum_adjacent_squares(square, xy):
    if xy == (0, 0):
        return 1

    neighbour_offsets = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    xy_neighbours = list(map(lambda o: tuple(numpy.add(xy, o)), neighbour_offsets))

    neighbours = { k:square[k] for k in xy_neighbours }

    return sum(n['value'] for n in neighbours.values() if 'value' in n)


def generate_matrix(inp=inp, stress_test=False):
    values = [{
        'value': 1,
        'x': 0,
        'y': 0,
    }]

    matrix = defaultdict(dict)
    square = defaultdict(dict)
    xy = {'x': 0, 'y': 0}
    position = itertools.count(1)
    distance = itertools.count()
    direction = itertools.cycle(['r', 'u', 'l', 'd'])
    coords = {
        'r': {'x': 1, 'y': 0},
        'u': {'x': 0, 'y': 1},
        'l': {'x':-1, 'y': 0},
        'd': {'x': 0, 'y':-1},
    }

    value = 0
    pos = next(position)
    dist = next(distance)
    dist_ctr = 0
    move = coords[next(direction)]

    while(value <= inp):
        matrix[pos].update(xy)
        value = sum_adjacent_squares(square, tuple(xy.values())) if stress_test else pos
        matrix[pos]['position'] = pos
        matrix[pos]['value'] = value
        square[tuple(xy.values())] = matrix[pos]
        
        if math.sqrt(pos).is_integer():
            dist = next(distance)

        if dist_ctr == dist:
            dist_ctr = 0
            move = coords[next(direction)]

        pos = next(position)
        dist_ctr += 1
        xy['x'] += move['x']
        xy['y'] += move['y']

    return matrix


def day_03(inp=inp):
    matrix = generate_matrix(inp)

    distance = abs(matrix[inp]['x']) + abs(matrix[inp]['y'])

    return {
        'stats': '',
        'result': distance,
    }


def day_03_part_2(inp=inp):
    matrix = generate_matrix(inp=inp, stress_test=True)
    
    value = matrix[len(matrix)]['value']

    return {
        'stats': '',
        'result': value,
    }
