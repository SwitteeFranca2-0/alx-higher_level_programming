#!/usr/bin/python3

if __name__ == "__main__":
    """Print arguments."""
    from sys import argv

    if (len(argv) > 2):
        print("{} arguments:".format(len(argv) - 1))
    elif (len(argv) == 2):
        print("1 argument:")
    else:
        print("0 arguments.")
    for arg in argv:
        if (argv.index(arg) != 0):
            print("{}: {}".format(argv.index(arg), arg))
