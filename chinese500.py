#!/usr/bin/python3

__doc__ = '''
Convert text file content chinese word
in order to input quizlet
'''

import re
INPUT = 'chinese500.in'
OUTPUT = 'chinese500.out'


def main():
    with open(INPUT, 'rt') as f_in:
        with open(OUTPUT, 'wt') as f_out:
            for line in f_in:
                f_out.write(line[line.find('.')+2:])


if __name__ == '__main__':
    main()