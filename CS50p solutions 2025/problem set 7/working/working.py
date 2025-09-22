import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        pattern = re.compile(r"(\d{1,2}(?::\d{2})?)\s(AM|PM)\sto\s(\d{1,2}(?::\d{2})?)\s(AM|PM)")

        match = pattern.match(s)

        if not match:
            raise ValueError

        time1, AMorPM1, time2, AMorPM2 = match.groups()

        if ':' in time1:
            retTimeHr1, retTimeMin1 = map(int, time1.split(':'))
            retTimeHr2, retTimeMin2 = map(int, time2.split(':'))
        else:
            retTimeHr1 = int(time1)
            retTimeMin1 = 0
            retTimeHr2 = int(time2)
            retTimeMin2 = 0

        if retTimeHr1 < 1 or retTimeHr1 > 12 or retTimeMin1 < 0 or retTimeMin1 > 59:
            raise ValueError

        if retTimeHr2 < 1 or retTimeHr2 > 12 or retTimeMin2 < 0 or retTimeMin2 > 59:
            raise ValueError

        if AMorPM1 == "AM":
            if retTimeHr1 == 12:
                retTimeHr1 = 0
        elif AMorPM1 == "PM":
            if retTimeHr1 != 12:
                retTimeHr1 += 12

        if AMorPM2 == "AM":
            if retTimeHr2 == 12:
                retTimeHr2 = 0
        elif AMorPM2 == "PM":
            if retTimeHr2 != 12:
                retTimeHr2 += 12

        return(f"{retTimeHr1:02d}:{retTimeMin1:02d} to {retTimeHr2:02d}:{retTimeMin2:02d}")

    except ValueError:
        sys.exit(ValueError)

if __name__ == "__main__":
    main()
