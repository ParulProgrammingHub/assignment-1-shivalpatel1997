def simple_interest(p,t,r):
    a=float(p*r*t/100)
    print "Simple interest is %f" %a
p=input("Enter principal amount")
r=input("Enter interest rate")
t=input("Enter time")
simple_interest(p,t,r)
