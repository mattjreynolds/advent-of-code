import days


def test_1():
    tests = [
        ('''ne,ne,ne''', 
        3),
        ('''ne,ne,sw,sw''', 
        0),
        ('''ne,ne,s,s''', 
        2),
        ('''se,sw,se,sw,sw''', 
        3),
        ('''ne,nw,ne,nw,nw''', 
        3),
    ]
    for t in tests:
        assert days.day_11(t[0])['result'] == t[1]
