a,b,c=0,1,0
num=7
if num<=0:
    print("cannot be negative terms")
elif num==1:
    print(b)
else:
    while c!=num:
        c=a+b
        print(c)
        a=b
        b=c
        c+=1