m1=input("Enter marks of subject1 out of 100")
m2=input("Enter marks of subject2 out of 100")
m3=input("Enter marks of subject3 out of 100")
m4=input("Enter marks of subject4 out of 100")
m5=input("Enter marks of subject5 out of 100")
s=m1+m2+m3+m4+m5
mean=float(s/5)
percent=float((s*100)/500)
print mean
print percent
if percent < 35 :
    print "Fail!"
else :
    print "Pass!"


