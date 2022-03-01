m1 = int(input("enter the subject1 mark"))
m2 = int (input("enter the subject2 mark"))
m3 =  int (input("enter the subject3 mark"))
m4 = int (input("enter the subject4 mark"))
m5 = int (input("enter the subject5 mark"))

total = m1+m2+m3+m4+m5
per = total*0.2
if per >=90 :
    print ("grade A")
elif per >=80 :
    print ("grade B")
elif per >=70 :
    print("grade c")
elif per>=60 :
    print("grade D")
elif per>=40 :
    print ("grade E")
else :
    print ("grade f")
