from seasons import dateToWords
import pytest
def main():
    pass

def test_dateToWords():
    assert dateToWords("2000-12-12")=="Twelve million, three hundred fifty-two thousand, three hundred twenty minutes"
    with pytest.raises(SystemExit) as error:
        dateToWords("hello i am under the water")
    assert str(error.value)=="Invalid date"
if __name__=="__main__":
    main()
