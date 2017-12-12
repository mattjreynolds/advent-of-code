import days


def test_1():
    tests = [
        ('''0 <-> 2
            1 <-> 1
            2 <-> 0, 3, 4
            3 <-> 2, 4
            4 <-> 2, 3, 6
            5 <-> 6
            6 <-> 4, 5''', 
        6),
    ]
    for t in tests:
        assert days.day_12(t[0])['result'] == t[1]


def test_2():
    tests = [
        ('''0 <-> 2
            1 <-> 1
            2 <-> 0, 3, 4
            3 <-> 2, 4
            4 <-> 2, 3, 6
            5 <-> 6
            6 <-> 4, 5''', 
        2),
    ]
    for t in tests:
        assert days.day_12_part_2(t[0])['result'] == t[1]
