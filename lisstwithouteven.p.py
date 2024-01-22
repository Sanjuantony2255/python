num=int(input("enter range:"))
list=[]
for i in range(num):
    number=int(input("enter numbers:"))
    if number%2!=0:
        list.append(number)
print(list)
