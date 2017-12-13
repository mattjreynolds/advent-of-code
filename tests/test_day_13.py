import days


def test_1():
    tests = [
        ('''0: 3
            1: 2
            4: 4
            6: 4 ''', 
        24),
    ]
    for t in tests:
        assert days.day_13(t[0])['result'] == t[1]


def test_2():
    tests = [
        ('''0: 3
            1: 2
            4: 4
            6: 4 ''', 
        10),
    ]
    for t in tests:
        assert days.day_13_part_2(t[0])['result'] == t[1]
