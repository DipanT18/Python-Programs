from datetime import date
from sys import exit
import inflect

def main():
    print(dateToWords(input("Date of Birth: ")))

def dateToWords(s):
    try:
        return (f"{(inflect.engine().number_to_words((int(((date.today()-date.fromisoformat(s)).days))*1440),andword="")).capitalize()} minutes")
    except ValueError:
        exit("Invalid date")

if __name__ == "__main__":
    main()
