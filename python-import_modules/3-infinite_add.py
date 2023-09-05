#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    fs = 0
    for i in range(len(sys.argv) - 1):
        fs += int(sys.argv[i +1])
    print ("{}".format(fs))
