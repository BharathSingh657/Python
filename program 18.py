"""Write a program to compute and display the temperature inside the
earth in Celsius and Fahrenheit. The relevant formulas are
Celsius = 10 x (depth) + 20
Fahrenheit = 1.8 x (Celsius) + 32"""


d = int(input("enter the depth "))

tc = (10*d)+20
tf = (1.8*tc)+32

print ("temperature in farenheit is " , tf)
print ("temperature in celsius is " , tc)
