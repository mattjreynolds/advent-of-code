import days

def test_1():
    tests = [
        ('''0
            3
            0
            1
            -3''', 
        5),
    ]
    for t in tests:
        assert days.day_05(t[0])['result'] == t[1]

def test_2():
    tests = [
        ('''0
            3
            0
            1
            -3''', 
        10),
    ]
    for t in tests:
        assert days.day_05_part_2(t[0])['result'] == t[1]
