def test_time():
    d = [1, 2]
    try:
        c = d[2]
        print d
    except IndexError:
        print "Else"
if __name__ == '__main__':
    test_time()
