#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:26:30 2022

@author: ousmanealhayri
"""

#!/usr/bin/python

from base import get_stream, close_stream

def reducer():
    max_value = 0
    old_key = None
    stream = get_stream()

    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Saut de ligne
            continue

        this_key, this_sale = data_mapped

        # cas particulier-premiére clés
        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print_result(max_value, old_key)
            old_key = this_key
            max_value = 0

        value = float(this_sale)

        if max_value < value:
            max_value = value

    # cas particuliére-deuxiéme clés
    print_result(max_value, old_key)

    close_stream(stream)


def print_result(max_value, old_key):
    print ("{0}\t{1}".format(old_key, max_value))


def main():
    reducer()


if __name__ == "__main__":
    main()