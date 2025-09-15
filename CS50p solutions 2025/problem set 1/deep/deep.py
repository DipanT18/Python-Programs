x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

match x:
    case "42":
        print("Yes")
    case "Forty Two":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")
