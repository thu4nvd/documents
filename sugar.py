#!/usr/bin/python3
__doc__ = '''
Dong nao chi chua so -> xoa dong
Dong trong -> xoa 
Dong nao chua chuoi "www.SachVui.Com" -> xoa dong
Dong nao bat dau bang chu cai in thuong thi xoa dau xuong dong cua dong truoc no, con khong thi giu nguyen
Neu ket thuc bang dau cham thi xuong dong.
'''

import string

def main():
    group = []
    with open("sugar.in", "rt") as ftxt:
        with open("sugar.out", "wt") as fout:
            for line in ftxt:
                if (line == '\n') or ("www.SachVui.Com" in line):
                    continue
                elif len(line) <5:
                    continue
                elif line[-2:] == '.\n':
                    group.append(line)
                    fout.write(' '.join(group))
                    group = []
                else: 
                    group.append(line[:-1])
            fout.write(' '.join(group))


if __name__ == "__main__":
    main()
