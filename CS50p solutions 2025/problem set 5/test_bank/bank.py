def main():
    x=input("Greeting: ")
    print(f"${value(x)}")


def value(greeting):
    if greeting.lower().strip().partition(" ")[0][:5]=="hello":
        return int(0)
    elif greeting.lower().strip().partition(" ")[0][0]=="h":
        return int(20)
    else:
       return int(100)


if __name__ == "__main__":
    main()


