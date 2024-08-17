"""Little Bob loves chocolate, and he goes to a store with Rs. Nin his
pocket. The price of each chocolate is Rs. C. The store offers a discount:
for every M wrappers he gives to the store, he gets one chocolate for
free. This offer is available only once. How many chocolates does Bob
get to eat? Write a program that solves this problem"""


r= int(input("enter the amount of money he has "))
c = int(input("enter the price of each chocolate "))



m = int(input("enter the amount of wrappers for a free chocolate "))


n = r//c


f = n//m


t= f+n


print("total number of chocolates he eats is ",t)


              


