import sys

def main():
    y=input("Fraction: ")
    print(gauge(convert(y)))

def convert(y):
    try:
        if "/" in y:
            x=y.split("/")
            if(len(x[0].split("."))==1 and len(x[1].split("."))==1  ):
                if(float(x[0])<float(x[1])):
                    result= round(float(x[0])/float(x[1])*100)
                    return result
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        sys.exit("incorrect value given")
    except ZeroDivisionError:
        sys.exit("cannot divide by zero")

def gauge(percentage):
    if (percentage==100 or percentage==99):
        return "F"
    if (percentage==0 or percentage==1 ):
        return "E"
    if (percentage<99):
        return (f"{percentage}%")

if __name__ == "__main__":
    main()

