from fuel import convert,gauge
import pytest

def main():
    pass

def test_fuel():
    assert convert("1/2")==50
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(0) == 'E'
    with pytest.raises(ValueError):
        convert("hello")
    with pytest.raises(ValueError):
        convert("9/1")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

if __name__=="__main__":
    main()
