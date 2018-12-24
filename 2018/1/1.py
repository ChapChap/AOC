def first():
    f = open('input', 'r')
    res = 0
    for line in f:
        res+=int(line)
    f.close()
    print(res)

def second():
    res = 0
    lst = set()
    while True:
        f = open('input', 'r')
        for line in f:
            lst.add(res)
            res+=int(line)
            if res in lst:
                print(res)
                exit(0)
        f.close()


first()
second()