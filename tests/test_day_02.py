import days

def test_1():
    tests = [
        ('''5 1 9 5
        7 5 3
        2 4 6 8''',
        '18'),
    ]
    for t in tests:
        assert days.day_02(t[0])['result'] == t[1]

def test_2():
    tests = [
        (
        '''5 9 2 8
        9 4 7 3
        3 8 6 5''',
        '9'),
    ]
    for t in tests:
        assert days.day_02_part_2(t[0])['result'] == t[1]
