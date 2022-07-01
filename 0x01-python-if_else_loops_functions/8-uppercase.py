#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for chr in str:
        if ord(chr) >= 97 and ord(chr) <= 122:
            cap = ord(chr) - 32
            print("{0:c}".format(cap), end="")
        else:
            print("{0}".format(chr), end="")
    print()
