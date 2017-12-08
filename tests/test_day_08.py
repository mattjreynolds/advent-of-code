import days

def test_1():
    tests = [
        ('''b inc 5 if a > 1
            a inc 1 if b < 5
            c dec -10 if a >= 1
            c inc -20 if c == 10''', 
        1),
    ]
    for t in tests:
        assert days.day_08(t[0])['result'] == t[1]

def test_2():
    tests = [
        ('''b inc 5 if a > 1
            a inc 1 if b < 5
            c dec -10 if a >= 1
            c inc -20 if c == 10''', 
        10),
    ]
    for t in tests:
        assert days.day_08_part_2(t[0])['result'] == t[1]
