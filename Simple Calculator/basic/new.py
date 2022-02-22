import math
sum=0
n=int(input('enter any number:'))
for i in range(1,n+1):
    sum=sum+(1/math.factorial(i))
print(sum)