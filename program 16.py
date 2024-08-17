"""Government of India has decided to give scholarships for students who
are first graduates in family and have scored average > 98 in math,
physics, and chemistry. Design an algorithm and write a Python
program to check if a student is eligible for scholarship. (Boundary
Conditions: All marks should be >0 )"""


m1 = int(input("enter the maths marks "))
m2 = int(input("enter the physics marks "))
m3 = int(input("enter the chemistry marks "))

sum = m1+m2+m2

avg = sum/3

if (avg > 98):
    print("eligible for scholarship ")
else :
    print("not eligible for scholarship ")
    
