# I'm using python v3.8 due to Windows 7 installed.
import math


x = 0
y = 0

TITLE = "SuperCalculator"

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def div(x, y):
    return x - y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))  

def log(x, y):
    return math.log(x, y)    

def sqrt(x,y):
    return math.pow(x, y)

def menu():
        print("Operations: ")
        print("Add: + ")
        print("Substr: - ")
        print("Div: / ")
        print("Sin: s ")
        print("Cos: c ")
        print("Power: p ")
        print("Log: l ")
        print("Exit: q ")
        return input("Your choice ( + | - | / | q | s | c | l | p ): ")


while True:
    o = menu()
    if o == 'q':
        print('Thank you for using ' + TITLE + '!' )
        break
    x = int(input('Enter x = '))
    if (o != 's' and o != 'c'):
        y = int(input('Enter y = '))
    


    if o == '+':
        print(plus(x, y))
    elif o == '-':
        print(minus(x, y))
    elif o == '/'and y == 0:
        print("Incorrect: division by zero")
    elif o == '/':    
        print(div(x, y))
    elif o == 's':    
        print(math.sin(math.radians(x)))
    elif o == 'c':    
        print(math.cos(math.radians(x)))
    elif o == 'l':
        print(math.log(x, y))
    elif o == 'p':
        print(math.pow(x, y))
    else:
        print('Wrong operation')

