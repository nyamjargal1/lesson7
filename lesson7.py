#2. A software company sells a package that retails for $99.
#Quantity discounts are given according to the following table:

#Quantity	Discount
#10–19	        10%
#20–49   	20%
#50–99	        30%
#100 or more	40%
#Write a program that asks the user to enter the number of
#packages purchased. The program should then display the
#amount of the discount (if any) and the total amount of
#the purchase after the discount.

y=99
x=int(input("Enter the number of packages purchased: "))
print("--------------------------------")
print("10-19 packages are 10% off")
print("20-49 packages are 20% off")
print("50-99 packages are 30% off")
print("100 or more packages are 40% off")
print("--------------------------------")
if x>=10 and x<=19:
    print("10% off, so the discount amount is", (y*x)*0.1, "dollar")
    print("The total amount of the purchase after the discount:", (y*x)-((y*x)*0.1), "dollar")
elif x>=20 and x<=49:
    print("20% off, so the discount amount is", (y*x)*0.2, "dollar",)
    print("The total amount of the purchase after the discount:", (y*x)-((y*x)*0.2), "dollar")
elif x>=50 and x<=99:
    print("30% off, so the discount amount is", (y*x)*0.3, "dollar")
    print("The total amount of the purchase after the discount:", (y*x)-((y*x)*0.3), "dollar")
elif x>100:
    print("40% off, so the discount amount is", (y*x)*0.4, "dollar")
    print("The total amount of the purchase after the discount:", (y*x)-((y*x)*0.4), "dollar")
print("End of the program.")