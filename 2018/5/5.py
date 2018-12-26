#!/usr/local/bin/python3
def index_double_letter(polymer):
    for i in range(1, len(polymer)):
        if polymer[i] != polymer[i - 1] and polymer[i].lower() == polymer[
                i - 1].lower():
            return i - 1
    return -1


def rec(polymer):
    index = index_double_letter(polymer)
    if index == -1:
        return polymer
    else:
        return rec(polymer[:index] + polymer[index + 2:])


def ite(polymer):
    index = index_double_letter(polymer)
    while index != -1:
        polymer = polymer[:index] + polymer[index + 2:]
        index = index_double_letter(polymer)
    return polymer


def one():
    f = open('input', 'r')
    polymer = f.readline()
    f.close()
    print(len(ite(polymer)))


def test():
    t = "dabAcCaCBAcCcaDA"
    s = "dabCBAcaDA"
    t1 = index_double_letter(t)
    if t1 != 4:
        print("Wrong test 1 ", t1)
    t2 = index_double_letter(s)
    if t2 != -1:
        print("Wrong test 2", t2)
    t3 = rec(t)
    if t3 != s:
        print("Wrong test 3", t3)
    itert = ite(t)
    if itert != s:
        print("Wrong test itert", itert)
    print("test done")


one()
#test()