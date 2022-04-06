
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:20:58 2022

@author: ousmanealhayri
"""
#!/usr/bin/python
from io import StringIO
import re
import sys


# ouverture du fichier si doné en argument
# et lire à partir de stdin
def get_stream(text=None):
    input_file = None

    if text is not None:
        return StringIO.StringIO(text)
    else:
        if len(sys.argv) == 2:
            input_file = sys.argv[1]

        if input_file:
            return open(input_file)
        else:
            return sys.stdin


# fermeture du fichier si donné comme entré
def close_stream(inf):
    try:
        inf.close()
    except:
        pass


def get_common_log_format():
    parts = [
        r'(?P<host>\S+)',  # host %h
        r'(?P<indent>\S+)',  # indent %l (unused)
        r'(?P<user>\S+)',  # user %u
        r'\[(?P<time>.+)\]',  # time %t
        r'"(?P<request>.*)"',  # request "%r"
        r'(?P<status>[0-9]+)',  # status %>s
        r'(?P<size>\S+)'
    ]

    pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')
    return pattern