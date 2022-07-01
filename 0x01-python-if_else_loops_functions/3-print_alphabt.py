#!/usr/bin/python3
ascii = 97
while ascii <= 122:
    if ascii != 101 and ascii != 113:
        print("{0:c}".format(ascii), end="")
    ascii += 1
