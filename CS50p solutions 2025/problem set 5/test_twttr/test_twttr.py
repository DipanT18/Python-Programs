from twttr import shorten

def main():
    pass

def test_twttr():
    assert shorten("hello")=="hll"
    assert shorten("Your")=="Yr"
    assert shorten("NUMBER")=="NMBR"
    assert shorten("1234")=="1234"
    assert shorten("right.")=="rght."

if __name__=="__main__":
    main()
