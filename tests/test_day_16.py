import days


def test_1():
    tests = [
        ('s1,x3/4,pe/b', 
        'abcde',
        'baedc'),
    ]
    for t in tests:
        assert days.day_16(t[0], t[1])['result'] == t[2]


def test_2():
    tests = [
        ('s1,x3/4,pe/b', 
        'abcde',
        'baedc'),
    ]
    for t in tests:
        assert days.day_16_part_2(t[0], t[1])['result'] == t[1]
