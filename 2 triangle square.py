import math

alfa = input('Enter angle alfa (degrees) = ')
beta = input('Enter angle beta (degrees) = ')
a = input('Enter adjacent side length (cm)= ' )

#s = ((int(a)**2) / 2) * (int(alfa) * int(beta)) / (180 - (int(alfa) + int(beta)))

s = ((int(a)**2) / 2) * math.sin(math.radians(int(alfa))) * math.sin(math.radians(int(beta))) / (math.sin(math.radians(180 - (int(alfa) + int(beta)))))

#s = (math.sin(math.radians(180 - (int(alfa) + int(beta)))))

print('Triangle square (cm*2) equals: ', s)




