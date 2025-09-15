import pyfiglet
import sys
import random

try:
    if len(sys.argv)==3:
        if sys.argv[1] != "-f":
            sys.exit("Invalid usage")
        else:
            font=sys.argv[2]
            if font in pyfiglet.FigletFont.getFonts():
                userInput=input("Input: ").strip()
                print("Output:")
                print(pyfiglet.Figlet(font=font).renderText(userInput))
            else:
                sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
except IndexError:
    userInput=input("Input: ").strip()
    print("Output:")
    print(pyfiglet.Figlet(font=random.choice(pyfiglet.FigletFont.getFonts())).renderText(userInput))
