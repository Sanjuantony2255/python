num=[12,100,20,130,56,121]
list=[]
for i in num:
    if(i in num and i>100):
        list.append('over')
    else:
        list.append(i)
print(list)
