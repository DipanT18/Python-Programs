x,y,z=input("Expression: ").lower().strip().split()

match y:
    case "+":
        a=float(x)+float(z)
    case "-":
        a=float(x)-float(z)
    case "/":
        a=float(x)/float(z)
    case "*":
        a=float(x)*float(z)

print(a)
