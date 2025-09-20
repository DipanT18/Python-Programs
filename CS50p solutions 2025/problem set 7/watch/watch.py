import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    hello=re.compile(r'embed/\w+"')
    try:
        return (f"https://youtu.be/{hello.findall(s)[0].strip('"').strip("embed/")}")
    except IndexError:
        return None
if __name__ == "__main__":
    main()
