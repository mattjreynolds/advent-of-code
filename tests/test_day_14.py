import days


def test_1():
    tests = [
        ('flqrgnkx', 
        8108),
    ]
    for t in tests:
        assert days.day_14(t[0])['result'] == t[1]


def test_2():
    tests = [
        ('flqrgnkx', 
        1242),
    ]
    for t in tests:
        assert days.day_14_part_2(t[0])['result'] == t[1]
