names=[]
adieu="Adieu, adieu, to"
while True:
    try:
        inputName=input("Name: ").strip()
        names.append(inputName)
    except (EOFError):
        if len(names)==1:
            for name in names:
                adieu+=" "+name
        if len(names)==2:
            for name in names:
                if name==names[-1]:
                    adieu+=" and "+name
                else:
                    adieu+=" " + name
        if len(names)>2:
            adieu+=" "+names[0]+","
            for name in names[1:-1]:
                adieu+=" "+name+","
            adieu+=" and "+names[-1]
        print(adieu)
        break


