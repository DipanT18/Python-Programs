from working import convert
import pytest
def main():
    pass

def test_convert():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("1:15 AM to 11:45 PM") == "01:15 to 23:45"
    assert convert("12:00 PM to 1:00 AM") == "12:00 to 01:00"
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    with pytest.raises(ValueError):
        convert("invalid time format")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 XX to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:99 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("")
if __name__ == "__main__":
    main()
