import days

def test_1():
    tests = [
        ('aa bb cc dd ee', 1),
        ('aa bb cc dd aa', 0),
        ('aa bb cc dd aaa', 1),
    ]
    for t in tests:
        assert days.day_04(t[0])['result'] == t[1]

def test_2():
    tests = [
        ('abcde fghij', 1),
        ('abcde xyz ecdab', 0),
        ('a ab abc abd abf abj', 1),
        ('iiii oiii ooii oooi oooo', 1),
        ('oiii ioii iioi iiio', 0),
    ]
    for t in tests:
        assert days.day_04_part_2(t[0])['result'] == t[1]
