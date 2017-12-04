import days

def test_1():
    tests = [
        ('1122', '3'),
        ('1111', '4'),
        ('1234', '0'),
        ('91212129', '9'),
    ]
    for t in tests:
        assert days.day_01(t[0])['result'] == t[1]

def test_2():
    tests = [
        ('1212', '6'),
        ('1221', '0'),
        ('123425', '4'),
        ('123123', '12'),
        ('12131415', '4'),
    ]
    for t in tests:
        assert days.day_01_part_2(t[0])['result'] == t[1]
