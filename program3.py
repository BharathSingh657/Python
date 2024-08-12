#Write a program to find the largest and smallest among 3 given numbers.

a = float(input ("Enter the first number ,a "))
b = float(input ("Enter the second number ,b"))
c = float(input ("Enter the third number ,c "))

if (a>b):
          if (a>c):
              print ("a is the largest number ")
          else:
              print ("c is the largest number ")

else :
          if (b>c):
              print ("b is the largest number ")
          else :
              print ("c is the largest number ")
              
