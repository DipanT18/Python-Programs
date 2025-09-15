def main():
    a = input("What time is it? ")
    x = convert(a)
    if x >= 7 and x <= 8:
        print("breakfast time")
    if x >= 12 and x <= 13:
        print("lunch time")
    if x >= 18 and x <= 19:
        print("dinner time")


def convert(time):
    return float(float(time.lower().strip().split(":")[0])+(float(time.lower().strip().split(":")[1])/60))


if __name__ == "__main__":
    main()
