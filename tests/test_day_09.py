import days


def test_1_group_count():
    tests = [
        ('''{}''', 
        1),
        ('''{{{}}}''', 
        3),
        ('''{{},{}}''', 
        3),
        ('''{{{},{},{{}}}}''', 
        6),
        ('''{<{},{},{{}}>}''', 
        1),
        ('''{<a>,<a>,<a>,<a>}''', 
        1),
        ('''{{<a>},{<a>},{<a>},{<a>}}''', 
        5),
        ('''{{<!>},{<!>},{<!>},{<a>}}''', 
        2),
    ]
    for t in tests:
        assert days.day_09(t[0])['group_count'] == t[1]


def test_1_group_scores():
    tests = [
        ('''{}''', 
        1),
        ('''{{{}}}''', 
        6),
        ('''{{},{}}''', 
        5),
        ('''{{{},{},{{}}}}''', 
        16),
        ('''{<a>,<a>,<a>,<a>}''', 
        1),
        ('''{{<ab>},{<ab>},{<ab>},{<ab>}}''', 
        9),
        ('''{{<!!>},{<!!>},{<!!>},{<!!>}}''', 
        9),
        ('''{{<a!>},{<a!>},{<a!>},{<ab>}}''', 
        3),
    ]
    for t in tests:
        assert days.day_09(t[0])['result'] == t[1]


def test_2():
    tests = [
        ('''<>''', 
        0),
        ('''<random characters>''', 
        17),
        ('''<<<<>''', 
        3),
        ('''<{!>}>''', 
        2),
        ('''<!!>''', 
        0),
        ('''<!!!>>''', 
        0),
        ('''<{o"i!a,<{i<a>''', 
        10),
    ]
    for t in tests:
        assert days.day_09_part_2(t[0])['result'] == t[1]