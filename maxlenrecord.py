a=[]
n=int(input("enter the size:"))
for i in range(1,n+1):
    name=input("enter the element:")
    a.append(name)
max1=len(a[0])
temp=a[0]
for i in a:
    if len(i)>max1:
        max1=len(i)
        temp=i
print("longest word is: ",temp," of length:",max1)
