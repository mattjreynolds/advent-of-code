import days

def test_1():
    tests = [
        (1, 0),
        (6, 1),
        (7, 2),
        (12, 3),
        (23, 2),
        (1024, 31),
    ]
    for t in tests:
        assert days.day_03(t[0])['result'] == t[1]

def test_2():
    tests = [
        (1, 2),
        (5, 10),
        (26, 54),
        (142, 147),
        (362, 747),
    ]
    for t in tests:
        assert days.day_03_part_2(t[0])['result'] == t[1]
