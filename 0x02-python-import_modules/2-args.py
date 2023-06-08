#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    print("{} argument{}{}".format(argc, 's' if argc != 1 else '', ':' if argc > 0 else '.'))

    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))
