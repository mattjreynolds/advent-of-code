import days


def test_1():
    tests = [
        ('3,4,1,5', 
        list(range(5)),
        12),
    ]
    for t in tests:
        assert days.day_10(t[0], t[1])['result'] == t[2]


def test_2_xor_hash():
    tests = [
        ([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22], 
        [64])
    ]
    for t in tests:
        assert days.day_10_dense_hash(t[0]) == t[1]


def test_2_hex():
    tests = [
        ([64, 7, 255], 
        '4007ff')
    ]
    for t in tests:
        assert days.day_10_int_list_to_hex_string(t[0]) == t[1]


def test_2():
    tests = [
        ('', 
        'a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017',
        '33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3',
        '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', 
        '63960835bcdc130f0b66d7ff4f6a5a8e'),
    ]
    for t in tests:
        assert days.day_10_part_2(t[0])['result'] == t[1]
