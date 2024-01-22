x=int(input("Enter the range"))
list=[]
a=input("enter the value to be count")
for i in range(0,x):
    name=input("enter the name")
    list.append(name)
count=0
for i in list:
    count=count+i.count(a)
print(count)
