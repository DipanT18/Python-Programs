from um import count


def main():
    pass


def test_count():
    assert count("um um um") == 3
    assert count("hello hi i dont know") == 0
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2


if __name__ == "__main__":
    main()
