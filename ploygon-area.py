from math import tan, pi
n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))
area = n * (side ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ",area)
