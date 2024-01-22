count=int(input("enter how much colors:"))
colorlist=[]
for i in range(count):
    color=input("enter colors:")
    colorlist.append(color)
print(colorlist[0],"",colorlist[-1])
