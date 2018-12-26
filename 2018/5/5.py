#!/usr/local/bin/python3
def index_double_letter(start, polymer):
    for i in range(start, len(polymer) - 1):
        if polymer[i] != polymer[i + 1] and polymer[i].lower() == polymer[
                i + 1].lower():
            return i
    return -1


def rec(polymer):
    index = index_double_letter(0, polymer)
    if index == -1:
        return polymer
    else:
        return rec(polymer[:index] + polymer[index + 2:])


def react(polymer):
    index = index_double_letter(0, polymer)
    while index != -1:
        polymer = polymer[:index] + polymer[index + 2:]
        index = index_double_letter(index - 1, polymer)
    return polymer


def filter(polymer, unit):
    res = ""
    for i in polymer:
        if i != unit.lower() and i != unit.upper():
            res += i
    return res


def one():
    f = open('input', 'r')
    polymer = f.readline()
    f.close()
    print(len(react(polymer)))


def two():
    f = open('input', 'r')
    polymer = f.readline()
    f.close()
    res = len(polymer)
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i)
        res = min(res, len(react(filter(polymer, i))))
        print(res)
    print(res)


def testone():
    t = "dabAcCaCBAcCcaDA"
    s = "dabCBAcaDA"
    t1 = index_double_letter(0, t)
    if t1 != 4:
        print("Wrong test 1 ", t1)
    t2 = index_double_letter(0, s)
    if t2 != -1:
        print("Wrong test 2", t2)
    t3 = rec(t)
    if t3 != s:
        print("Wrong test 3", t3)
    itert = react(t)
    if itert != s:
        print("Wrong test itert", itert)
    print("test done")


def testtwo():
    t = "dabAcCaCBAcCcaDA"
    s = "dbCBcD"
    t1 = 'd'.lower() in t or 'd'.upper() in t
    if not t1:
        print("Wrong test t1", t1)
    t2 = 'a'.lower() in s or 'a'.upper() in s
    if t2:
        print("Wrong test t2", t2)
    t3 = filter(t, 'a')
    if t3 != "dbcCCBcCcD":
        print("Wrong test t3", t3)
    t4 = react(t3)
    if t4 != s:
        print("Wrong test t4", t4)
    t5 = len(t)
    for i in "abcdefghijklmnopqrstuvwxyz":
        t5 = min(t5, len(react(filter(t, i))))
    if t5 != 4:
        print("Wrong test t5", t5)
    print("test done")


#testone()
one()
#testtwo()
#two()