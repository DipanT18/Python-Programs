due=50

while due>0:
    print(f"Amount Due: {due}")

    coin=int(input("Insert coin:"))
    match coin:
        case 25:
            due-=25
        case 10:
            due-=10
        case 5:
            due-=5
        case _:
            continue
    if due<=0:
        owned=abs(due)
        print(f"Change Owed: {owned}")

