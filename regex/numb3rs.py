import re
import sys


def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except KeyboardInterrupt:
        sys.exit()


def validate(ip):
    regex_IPaddress = re.compile(r"^(25[0-5]|[1]?[0-9]?[0-99])\.(25[0-5]|[1]?[0-9]?[0-99])\.(25[0-5]|[1]?[0-9]?[0-99])\.(25[0-5]|[1]?[0-9]?[0-99])$")
    if regex_IPaddress.search(ip):
        return True
    return False


if __name__ == "__main__":
    main()