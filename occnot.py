x=int(input("enter the range"))
list=[]
for i in range(0,x):
    a=int(input("enter the values"))
    if a>100:
        list.append('over')
    else:
        list.append(a)
print(list)
