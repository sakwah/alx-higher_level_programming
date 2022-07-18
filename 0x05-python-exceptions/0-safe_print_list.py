#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for n in range(0, x):
            print("{}".format(my_list[n]), end="")
            i = i + 1
            if n == x - 1:
                print()
    except IndexError:
        print()
    finally:
        return i
