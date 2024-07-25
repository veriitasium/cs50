import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(src):
    if mobject := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", src):
        return f"https://youtu.be/{mobject.group(1)}"
    return None


if __name__ == "__main__":
    main()