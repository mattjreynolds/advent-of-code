import days


def test_1():
    tests = [
        ({
            'Generator A': 65,
            'Generator B': 8921,
        }, 
        588),
    ]
    for t in tests:
        assert days.day_15(t[0])['result'] == t[1]


def test_2():
    tests = [
        ({
            'Generator A': 65,
            'Generator B': 8921,
        }, 
        309),
    ]
    for t in tests:
        assert days.day_15_part_2(t[0])['result'] == t[1]
