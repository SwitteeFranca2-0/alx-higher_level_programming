#!/usr/bin/python3

"""Print arguments."""

if __name__ == "__main__":
		
	import sys

	if (len(sys.argv) != 1):
		print("{} arguments:".format(len(sys.argv)))
		for arg in sys.argv:
			if (sys.argv.index(arg) != 0):
				print("{}: {}".format(sys.argv.index(arg), arg))
	else:
		print("0 arguments.")
	