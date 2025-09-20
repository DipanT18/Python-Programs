from numb3rs import validate

def main():
    pass

def test_numb3rs():
    assert validate("192.168.1.1")==True
    assert validate("255.255.255.255")==True
    assert validate("192.168.40.89")==True
    assert validate("255.255.255.435")==False
    
if __name__ == "__main__":
    main()
