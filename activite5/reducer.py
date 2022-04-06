#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:35:18 2022

@author: ousmanealhayri
"""

#!/usr/bin/python

from base import get_stream, close_stream

test_text = """alfa\t5
alfa\t7
beta\t3.0
beta\t1 
"""
def reducer():
    value_total = 0
    old_key = None

    stream = get_stream()
    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # sauter la ligne.
            continue
       
        this_key, this_value = data_mapped
        
        # cas particulier -premier clés
        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print_result(old_key, value_total)
            old_key = this_key
            value_total = 0

        value_total += float(this_value)

    # cas particulier-deuxiéme clé
    print_result(old_key, value_total)

    close_stream(stream)  

def print_result(old_key, value_total):
    print ("{0}\t{1}".format(old_key, value_total))


def main():
    reducer()


if __name__ == "__main__":
    main()