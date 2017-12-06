import days

def test_1():
    tests = [
        ('''0 2 7 0''', 
        5),
    ]
    for t in tests:
        assert days.day_06(t[0])['result'] == t[1]

def test_2():
    tests = [
        ('''0 2 7 0''', 
        4),
    ]
    for t in tests:
        assert days.day_06_part_2(t[0])['result'] == t[1]
