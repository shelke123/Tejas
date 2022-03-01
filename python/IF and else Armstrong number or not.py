a= int (input("enter any three digit number"))
b= a//100
c=a%100
d=c//10
e=c%10
f= b**3+d**3+e**3
if f==a :
    print ("a is armstrong number")
else :
    print ("a is not armstrong number ")
