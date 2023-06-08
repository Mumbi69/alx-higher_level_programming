#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    total = 0
    for arg in argv:
        total += int(arg)
    print(total)
