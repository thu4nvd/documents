#!/usr/bin/python3

import re

def main():
    with open("vidu.txt", "rt") as ftxt:
        with open("vidu.out", "wt") as fout:
            for line in ftxt:
                fout.write(re.sub(' +', ' ', line))


if __name__ == "__main__":
    main()
