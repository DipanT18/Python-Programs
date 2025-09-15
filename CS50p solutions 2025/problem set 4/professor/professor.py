import random

def main():
    level=get_level()
    score=0
    for i in range(10):
        trys=0
        x=generate_integer(level)
        y=generate_integer(level)
        while trys<3:
            ans=x+y
            try:
                userAns=int(input(f"{x} + {y} = "))
                if(userAns==ans):
                    score+=1
                    break
                else:
                    print("EEE")
                    trys+=1
            except ValueError:
                pass
            if (trys==3):
                print(f"{x} + {y} = {ans}")
                break

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            userLevel=int(input("Level:").strip().lower())
            if(userLevel>3 or userLevel<=0):
                raise ValueError
            break
        except ValueError:
            pass

    return userLevel

def generate_integer(level):
    lb=0
    ub=0
    if(level==1):
        lb=0
        ub=9
    if(level==2):
        lb=10
        ub=99
    if(level==3):
        lb=100
        ub=999
    return random.randint(lb,ub)

if __name__ == "__main__":
    main()
