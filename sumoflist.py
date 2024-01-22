num=int(input("enter the range:"))
list1=[]
for i in range(num):
    value=int(input("enter numbers that you want to insert:"))
    list1.append(value)
sumoflist=0
for i in range(num):
    sumoflist=sumoflist+list1[i]
print("sum is",sumoflist)

    
