n=int(input('how many element?'))
a=[]
for i in range(1,n+1):
    item=int(input('enter a lememt'))
    a.append(item)
print(a)
print(max(a))