#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i and j != 0:
            if i == 8 and j == 9:
                print("{0:d}{1:d}".format(i, j))
            else:
                print("{0:d}{1:d}".format(i, j), end=", ")
