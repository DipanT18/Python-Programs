def main():
    x=input("Input: ").strip()
    print(f"Output: {shorten(x)}")


def shorten(x):
    buff=""
    for i in x:
        if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!="A" and i!="E" and i!="I" and i!="O" and i!="U":
            buff+=i
    return buff

if __name__ == "__main__":
    main()
