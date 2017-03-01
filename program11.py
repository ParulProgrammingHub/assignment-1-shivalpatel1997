def compound_interest(p,t,r):
    a=float(p*(1+(r/n))**(n*t))
    print "Compund interest is %f" %a
p=input("Enter principal amount")
r=float(input("Enter interest rate"))
r=r/100
n=float(input("Enter number of times the interest is compounded per year"))
t=float(input("Enter time"))
compound_interest(p,t,r)

