x=int(input("enter the range:"))
list=[]
for i in range(0,x):
    name=input("enter the name:")
    list.append(name)
count=0
for i in list:
    count=count+i.count("a")
print(count)
