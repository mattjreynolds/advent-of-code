inp = 'hfdlxzhv'

import days
import itertools
from collections import defaultdict


def day_14_int_list_to_bin_string(l):
    return ''.join([f'{x:08b}' for x in l])


def day_14_replace_region(dest, source, region_coords, regions, new_row):
    for x, y in region_coords[dest]:
        region_coords[source].append((x,y))
        if len(regions) == y:
            new_row[x] = source
        else:
            regions[y][x] = source
    del region_coords[dest]


def day_14(inp=inp, nums=list(range(256))):
    total = 0
    input_nums = nums
    grid = []
    for row in range(128):
        nums = input_nums
        lengths = [ord(l) for l in (inp.strip()+f'-{row}')] + [17,31,73,47,23]
        nums = days.day_10_reverse_bits(lengths, nums, rounds=64)
        dh = days.day_10_dense_hash(nums)
        bs = day_14_int_list_to_bin_string(dh)
        grid.append(bs)
        total += bs.count('1')

    return {
        'stats': '',
        'grid': grid,
        'result': total,
    }


def day_14_part_2(inp=inp, nums=list(range(256))):
    ret = day_14(inp, nums)
    regions = []
    region_coords = defaultdict(list)
    region_counter = itertools.count(1)
    for y, row in enumerate(ret['grid']):
        last_square = 0
        new_row = []
        for x, square in enumerate(row):
            square = int(square)
            if square:
                above = regions[y-1][x] if y else None
                square = (
                    above
                    if above else
                    last_square
                    if last_square else
                    next(region_counter)
                )
                region_coords[square].append((x, y))
                if last_square != square:
                    day_14_replace_region(last_square, square, region_coords, regions, new_row)

            last_square = square
            new_row.append(square)
        regions.append(new_row)

    ret['result'] = len(region_coords)
    return ret

