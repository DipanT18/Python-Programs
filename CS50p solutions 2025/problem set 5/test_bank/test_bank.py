from bank import value

def main():
    pass


def test_bank():
    assert value("hello")==0
    assert value("hey")==20
    assert value("no")==100
    assert value("HELLO hwoo")==0

if __name__ == "__main__":
    main()

