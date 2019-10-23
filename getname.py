#Bryan Morris
#9/25/19
#

def getName():
    while True:
        name = input("What is your name?")
        if " " in name:
            name = name.replace(" ", "QZRX")
        if name.isalpha():
            name = name.replace("QZRX", " ")
            name = name.title()
            return name
        else:
            print("Invalid syntax")

def mathFun(x,y):
    if x.isdigit() and y.isdigit() and len(x)  <= 2 and len(y)  <= 3 :
        x=int(x)
        y=int(y)
    else:
            print("Invalid syntax")
            return "you suck at math"
    num1 = x
    num2 = y
    total = num1*num2
    return total

x = input("enter a number")
y = input("enter a number")
result = mathFun(x,y)
print(result)
