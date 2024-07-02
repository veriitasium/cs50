import sys

def sys_arg_len(length = 2):
    if len(sys.argv) < length:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > length:
        sys.exit("Too many command-line arguments")