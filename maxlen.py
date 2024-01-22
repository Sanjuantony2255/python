a=[]
n=int(input("enter the size:"))
for i in range(1,n+1):
    name=input("enter the element:")
    a.append(name)
z=max(a,key=len)
print("longest word is:",z,"of length",len(z))
