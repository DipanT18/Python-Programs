import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = re.compile(r"(?i)\bum\b")
    matches = pattern.findall(s)
    print(matches)
    return len(matches)


if __name__ == "__main__":
    main()
