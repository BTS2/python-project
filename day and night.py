a = input("Enter hours = ")
b = input("Enter minutes = ")
c = input("Enter difference in minutes = ")

d = int(a) * 60 + int(b) + int(c)


def convert(min):
    min = min % (24 * 60)
    hour = min // 60
    min %= 60

 
    print("minutes value in hours:",hour)
    print("minutes value in minutes:",min)
    return "%02d:%02d" % (hour, min)

n = d
print("Time is now : ", convert(n))

