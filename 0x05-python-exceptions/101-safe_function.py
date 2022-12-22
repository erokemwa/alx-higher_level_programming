#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as st:
        print("Exception: {}".format(st), file=sys.stderr)
