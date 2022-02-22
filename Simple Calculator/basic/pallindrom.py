num=int(input('enter any number:'))
temp=num
rev_num=0
while rev_num !=0:
    digit=num%10
    rev_num=rev_num*10+digit
    num=num//10
if temp==rev_num:
       print("the num is pallindrom")
else:
       print("the num is not pallindrom")
