#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:20:11 2022

@author: ousmanealhayri
"""

#!/usr/bin/python

from base import get_stream, close_stream


def mapper():
    inf = get_stream()

    for line in inf:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print("{0}\t{1}".format(item, cost))

    close_stream(inf)


def main():
    mapper()


if __name__ == "__main__":
    main()