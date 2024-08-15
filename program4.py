import math
a = int(input("Enter the Length of the first side "))
b = int(input("Enter the length of the second side "))
c = int(input("Enter the length of the third side "))
s = (a+b+c)/2
area = math.sqrt( s*(s-a)*(s-b)*(s-c))
print ("area of the triangle is " , area)
