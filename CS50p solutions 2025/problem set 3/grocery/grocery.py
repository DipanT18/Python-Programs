rawList = []
finalList = {}
while True:
    try:
        item = input().strip().upper()
        rawList.append(item)
    except EOFError:
        break
rawList = sorted(rawList)
for listItem in rawList:
    if listItem in finalList:
        finalList[listItem] += 1
    else:
        finalList[listItem]= 1
for item in finalList:
    print(f"{finalList[item]} {item}")
