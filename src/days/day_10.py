inp = '227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144'

import itertools
import operator
from functools import reduce


def day_10_dense_hash(l):
    chunk = 16
    chunks = [l[i:i+chunk] for i in range(0, len(l), chunk)]
    return [reduce(operator.xor, x) for x in chunks]


def day_10_int_list_to_hex_string(l):
    return ''.join([f'{x:02x}' for x in l])


def day_10_reverse_bits(lengths, nums, rounds=1):
    pos = 0
    skip = 0
    nl = len(nums)

    for i in range(rounds):
        for l in lengths:
            if l > len(nums):
                continue
            start = pos % len(nums)
            end = (pos + l) % len(nums)

            s1 = min(start, end)
            s2 = max(start, end)

            a = nums[:s1]
            b = nums[s1:s2]
            c = nums[s2:]

            if start <= end:
                b = b[::-1]
            else:
                ac = (c+a)[::-1]
                a = ac[len(c):]
                c = ac[:len(c)]

            nums = a + b + c

            pos += l + skip
            skip += 1

    return nums


def day_10(inp=inp, nums=list(range(256))):
    lengths = [int(l) for l in inp.split(',')]
    nums = day_10_reverse_bits(lengths, nums)
    return {
        'stats': '',
        'result': nums[0] * nums[1],
    }


def day_10_part_2(inp=inp, nums=list(range(256))):
    lengths = [ord(l) for l in inp.strip()] + [17,31,73,47,23]
    nums = day_10_reverse_bits(lengths, nums, rounds=64)
    dh = day_10_dense_hash(nums)
    hs = day_10_int_list_to_hex_string(dh)

    return {
        'stats': '',
        'result': hs,
    }

