def menu():
    print("Operations")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("q to quit")

o = ("Enter at least 2 numbers, separate each number by space. ")

def add():
    numlist = input(o).split()
    numlist = [float(num) for num in numlist]
    num1 = numlist[0]
    del numlist[0]
    for num in numlist:
        num1 = num1 + num
    return num1   

def sub():  
    numlist = input(o).split()
    numlist = [float(num) for num in numlist]
    num1 = numlist[0]
    del numlist[0]
    for num in numlist:
        num1 = num1 - num
    return num1

def mult():   
    numlist = input(o).split()
    numlist = [float(num) for num in numlist]
    num1 = numlist[0]
    del numlist[0]
    for num in numlist:
        num1 = num1 * num
    return num1

def div():   
    numlist = input(o).split()
    numlist = [float(num) for num in numlist]
    num1 = numlist[0]
    del numlist[0]
    for num in numlist:
        num1 = num1 / num
    return num1

menu()

operator = input("Please enter an operator: ")

while operator != "q":

    if operator == "+":
        print(add())
    elif operator == "-":
        print(sub())
    elif operator == "*":
       print(mult())
    elif operator == "/":
        print(div())
    menu()
    operator = input("Please enter an operator")    

print("Thank you for using calculator. See you next time.")
