#!/usr/local/bin/python3
import numpy as np


def read_coor(filename):
    f = open(filename, 'r')
    coordinates = []
    for line in f:
        coord = line.strip().split(", ")
        coordinates.append((int(coord[0]), int(coord[1])))
    f.close
    return coordinates


def input_to_grid(coordinates):
    from operator import itemgetter
    nlines = max(coordinates, key=itemgetter(1))[0] + 1
    ncol = max(coordinates, key=itemgetter(1))[1] + 1
    grid = np.zeros((nlines, ncol), dtype=np.int32)
    remaining_coor = []
    for i in range(nlines):
        for j in range(ncol):
            remaining_coor.append((i, j))
    for i, c in enumerate(coordinates):
        grid[c[0]][c[1]] = i + 1
        remaining_coor.remove((c[0], c[1]))
    return grid, remaining_coor


def is_equidist(c, A, B):
    distcA = abs(c[0] - A[0]) + abs(c[1] - A[1])
    distcB = abs(c[0] - B[0]) + abs(c[1] - B[1])
    return distcA == distcB


def boudaries(coordinates, grid, remaining_coor):
    for i, c1 in enumerate(coordinates):
        for j in range(i + 1, len(coordinates)):
            c2 = coordinates[j]
            dist = abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])
            print(i, c1, j, c2, dist)
            if dist % 2 == 0:
                for x in range(min(c1[0]), max(c2[0])):
                    for y in range(min(c1[1]), max(c2[1])):
                        if g[x][y] != -1:
                            if is_equidist((x, y), c1, c2):
                                g[x][y] = -1


c = read_coor("inputtest")
g, r = input_to_grid(c)
print(g)
#print(r)
boudaries(c, g, r)
print(g)