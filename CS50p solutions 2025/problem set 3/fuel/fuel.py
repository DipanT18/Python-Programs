while True:
    try:
        y=input("Fraction: ")
        if "/" in y:
            x=y.split("/")
            if(len(x[0].split("."))==1 and len(x[1].split("."))==1  ):
                if (round((float(x[0])/float(x[1]))*100)==100 or round(float(x[0])/float(x[1])*100)==99):
                    print("F")
                    break
                if (round((float(x[0])/float(x[1]))*100)==0 or round(float(x[0])/float(x[1])*100)==1 ):
                    print("E")
                    break
                if (round((float(x[0])/float(x[1]))*100)<99):
                    print(f"{round((float(x[0])/float(x[1]))*100)}%")
                    break
    except (ValueError, ZeroDivisionError):
        continue
