#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        ret = None

    return (ret)
