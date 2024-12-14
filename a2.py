#inputting values into the formula
PV = float(input("Enter the starting principal: "))
R =  float(input("Enter the annual interest rate: "))
m = float(input("How many times per year is the interest compunded? "))
t = float(input("For how many years will the account earn interest? "))
#rate conversion from whole number to decimal
RC = R / 100
#compounding interest formula
FV = PV*(1+RC/m)**(m*t)
#formatted print statement outputting what was plugged into the formula
print(f"At the end of {int(t)} years you will have $ {FV:,.2f}")