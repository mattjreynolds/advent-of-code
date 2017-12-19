import days


def test_1():
    tests = [
        (3, 
        638),
    ]
    for t in tests:
        assert days.day_17(t[0])['result'] == t[1]


def test_2():
    tests = [
        (3, 
        1222153),
    ]
    for t in tests:
        assert days.day_17_part_2(t[0])['result'] == t[1]
