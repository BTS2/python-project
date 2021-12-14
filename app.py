# comment

a = input("Enter a = ")
b = input("Enter b = ")

o = '%'
if o == '+':
    c = int(a) + int(b)

elif o == '-':
    c = int(a) - int(b)

elif o == '*':
    c = int(a) * int(b)

elif o == '//':
    c = int(a) // int(b)

elif o == '**':
    c = int(a) ** int(b)

elif o == '%':
    c = int(a) % int(b)

print()
print("a"+ o + "b=", c)