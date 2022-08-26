#!/usr/bin/python3


if __name__ == "__main__":
    """Sum arguments."""
    import sys
    sum = 0

    for arg in sys.argv:
        if (sys.argv.index(arg) != 0):
            sum += int(arg)

    print("{}".format(sum))
