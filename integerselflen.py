n1=int(input("Enter the range"))
list1=[]
for i in range(0,n1):
    a=int(input("enter the values"))
    list1.append(a)
n2= int(input("Enter the range"))
list2=[]
for i in range(0,n2):
    b=int(input("enter the values"))
    list2.append(b)
if(len(list1)==len(list2)):
    print("Same len")
else:
    print("not same")
if(sum(list1)==sum(list2)):
    print("Same sum")
else:
    print("not same")
list3=[each for each in list1 if each in list2]
print("same members are:",list3)
            
    
